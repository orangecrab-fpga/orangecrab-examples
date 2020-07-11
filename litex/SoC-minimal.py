#!/usr/bin/env python3

# This file is Copyright (c) Greg Davill <greg.davill@gmail.com>
# License: BSD


# This variable defines all the external programs that this module
# relies on.  lxbuildenv reads this variable in order to ensure
# the build will finish without exiting due to missing third-party
# programs.
LX_DEPENDENCIES = ["riscv", "nextpnr-ecp5", "yosys"]

# Import lxbuildenv to integrate the deps/ directory
import lxbuildenv

import sys
import os

from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex_boards.platforms import orangecrab
from litex_boards.targets.orangecrab import _CRG

from litex.soc.cores.clock import *
from litex.soc.integration.soc_core import *
from litex.soc.integration.soc_sdram import *
from litex.soc.integration.builder import *


# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    def __init__(self):
        # Board Revision ---------------------------------------------------------------------------
        sys_clk_freq=int(48e6)
        platform = orangecrab.Platform(toolchain='trellis')

        # SoCCore ----------------------------------------------------------------------------------
        SoCCore.__init__(self, platform, clk_freq=sys_clk_freq, csr_data_width=32, uart_name='stub', integrated_rom_size=32*1024)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = crg = _CRG(platform, sys_clk_freq)


# Build --------------------------------------------------------------------------------------------
def main():
    soc = BaseSoC()
    builder = Builder(soc)
    # Build gateware
    vns = builder.build()
    soc.do_exit(vns)   


if __name__ == "__main__":
    main()
