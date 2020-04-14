#!/usr/bin/env python3



#!/usr/bin/env python3

# This file is Copyright (c) Greg Davill <greg.davill@gmail.com>
# License: BSD

import sys
import os
import shutil
import argparse


import inspect

from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex_boards.platforms import orangecrab
from litex_boards.targets.orangecrab import _CRG

from litex.build.lattice.trellis import trellis_args, trellis_argdict

from litex.soc.cores.clock import *
from litex.soc.integration.soc_core import *
from litex.soc.integration.soc_sdram import *
from litex.soc.integration.builder import *

from litedram.modules import MT41K64M16, MT41K128M16, MT41K256M16
from litedram.phy import ECP5DDRPHY


from rtl.rgb import RGB
from litex.soc.cores import spi_flash

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    csr_map = {
        "ctrl":           0,  # provided by default (optional)
        "crg":            1,  # user
        "identifier_mem": 4,  # provided by default (optional)
        "timer0":         5,  # provided by default (optional)
        "usb":            9,
        "rgb":            13,
        "version":        14,
        "lxspi":          15,
        "button":         17,
    }
    csr_map.update(SoCCore.csr_map)

    mem_map = {
        "rom":      0x00000000,  # (default shadow @0x80000000)
        "sram":     0x10000000,  # (default shadow @0xa0000000)
        "spiflash": 0x20000000,  # (default shadow @0xa0000000)
        "main_ram": 0x40000000,  # (default shadow @0xc0000000)
        "csr":      0xe0000000,  # (default shadow @0xe0000000)
    }
    mem_map.update(SoCCore.mem_map)

    interrupt_map = {
        "timer0": 2,
        "usb": 3,
    }
    interrupt_map.update(SoCCore.interrupt_map)

    def __init__(self, sys_clk_freq=int(48e6), toolchain="trellis", **kwargs):
        # Board Revision ---------------------------------------------------------------------------
        revision = kwargs.get("revision", "0.2")
        device = kwargs.get("device", "25F")

        platform = orangecrab.Platform(revision=revision, device=device ,toolchain=toolchain)

        # Serial -----------------------------------------------------------------------------------
        platform.add_extension(orangecrab.feather_serial)

        # SoCCore ----------------------------------------------------------------------------------
        SoCCore.__init__(self, platform, clk_freq=sys_clk_freq, csr_data_width=32, **kwargs)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform, sys_clk_freq, with_usb_pll=True)

        # DDR3 SDRAM -------------------------------------------------------------------------------
        if not self.integrated_main_ram_size:
            available_sdram_modules = {
                'MT41K64M16': MT41K64M16,
                'MT41K128M16': MT41K128M16,
                'MT41K256M16': MT41K256M16,
#                'MT41K512M16': MT41K512M16 # Todo push definition for this part
            }
            sdram_module = available_sdram_modules.get(
                kwargs.get("sdram_device", "MT41K64M16"))

            self.submodules.ddrphy = ECP5DDRPHY(
                platform.request("ddram"),
                sys_clk_freq=sys_clk_freq)
            self.add_csr("ddrphy")
            self.add_constant("ECP5DDRPHY")
            self.comb += self.crg.stop.eq(self.ddrphy.init.stop)
            self.add_sdram("sdram",
                phy                     = self.ddrphy,
                module                  = sdram_module(sys_clk_freq, "1:2"),
                origin                  = self.mem_map["main_ram"],
                size                    = kwargs.get("max_sdram_size", 0x40000000),
                l2_cache_size           = kwargs.get("l2_size", 8192),
                l2_cache_min_data_width = kwargs.get("min_l2_data_width", 128),
                l2_cache_reverse        = True
            )

        # RGB LED
        led = platform.request("rgb_led", 0)
        self.submodules.rgb = RGB(led)

        # The litex SPI module supports memory-mapped reads, as well as a bit-banged mode
        # for doing writes.
        spi_pads = platform.request("spiflash4x")
        self.submodules.lxspi = spi_flash.SpiFlashDualQuad(spi_pads, dummy=6, endianness="little")
        self.lxspi.add_clk_primitive(platform.device)
        self.register_mem("spiflash", self.mem_map["spiflash"], self.lxspi.bus, size=16*1024*1024)


        # USB with Clock-Domain-Crossing support
        os.system("git clone https://github.com/gregdavill/valentyusb -b hw_cdc_eptri")
        sys.path.append("valentyusb")

        from valentyusb.usbcore import io as usbio
        from rtl.csr_cdc import CSRClockDomainWrapper
        usb_pads = platform.request("usb")
        usb_iobuf = usbio.IoBuf(usb_pads.d_p, usb_pads.d_n, usb_pads.pullup)
        self.submodules.usb0 = CSRClockDomainWrapper(usb_iobuf)
        self.comb += self.cpu.interrupt[self.interrupt_map['usb']].eq(self.usb0.irq)

        from litex.soc.integration.soc_core import SoCRegion
        self.bus.add_slave('usb',  self.usb0.bus, SoCRegion(origin=0x90000000, size=0x1000, cached=False))

        self.constants["FLASH_BOOT_ADDRESS"] = self.mem_map['spiflash'] + 0x00140000

    # Generate the CSR for the USB
    def write_usb_csr(self, directory):
        csrs = self.usb0.get_csr()

        from litex.soc.integration import export
        from litex.build.tools import write_to_file
        from litex.soc.integration.soc_core import SoCCSRRegion
        os.makedirs(directory, exist_ok=True)
        write_to_file(
            os.path.join(directory, "csr_usb.h"),
            export.get_csr_header({"usb" : SoCCSRRegion(0x90000000, 32, csrs)}, self.constants)
        )


# Build --------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LiteX SoC on OrangeCrab")
    parser.add_argument("--gateware-toolchain", dest="toolchain", default="trellis",
        help="gateware toolchain to use, trellis (default) or diamond")
    builder_args(parser)
    soc_sdram_args(parser)
    trellis_args(parser)
    parser.add_argument("--sys-clk-freq", default=48e6,
                        help="system clock frequency (default=48MHz)")
    parser.add_argument("--revision", default="0.2",
                        help="Board Revision {0.1, 0.2} (default=0.2)")
    parser.add_argument("--device", default="25F",
                        help="ECP5 device (default=25F)")
    parser.add_argument("--sdram-device", default="MT41K64M16",
                        help="ECP5 device (default=MT41K64M16)")
    args = parser.parse_args()

    print(argdict(args))
    soc = BaseSoC(toolchain=args.toolchain, sys_clk_freq=int(float(args.sys_clk_freq)), **argdict(args))
    builder = Builder(soc, **builder_argdict(args))
    soc.write_usb_csr(builder.generated_dir)
    builder_kargs = trellis_argdict(args) if args.toolchain == "trellis" else {}
    builder.build(**builder_kargs)

    input_config = os.path.join(builder.gateware_dir, "top.config")
    output_bitstream = os.path.join(builder.gateware_dir, "ecp_bitstream.bit")
    os.system(f"ecppack --spimode qspi --freq 38.8 --compress --input {input_config} --bit {output_bitstream}")

    dfu_file = os.path.join(builder.gateware_dir, "ecp5.dfu")
    shutil.copyfile(output_bitstream, dfu_file)
    os.system(f"dfu-suffix -v 1209 -p 5bf0 -a {dfu_file}")

def argdict(args):
    r = soc_sdram_argdict(args)
    for a in ["device", "revision", "sdram_device"]:
        arg = getattr(args, a, None)
        if arg is not None:
            r[a] = arg
    return r

if __name__ == "__main__":
    main()
