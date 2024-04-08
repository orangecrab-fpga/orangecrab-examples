# OrangeCrab example projects
This repository contains example code to be run on the OrangeCrab.

---

## RISCV examples
These examples make use of the Vexriscv CPU created inside the FPGA by the bootloader. The RISCV firmware is copied across into the FLASH by the bootloader. If the bootloader determines that it has not loaded new gateware, then the CPU will simply adjust it's program counter to start executing the newly loaded programs.

* __riscv.blink__ - The most basic example. Blink a LED with RISCV firmware
* __riscv.button__ - Read button input and toggle LED colour 

## Verilog examples
These examples use Yosys + NextPnR, to synthesis (or compile) verilog into a bitstream. A nice term for this is gateware. Since it is analogous to firmware, but describes how the FPGA needs to be configured. 

This gateware can be loaded onto the OrangeCrab using its DFU bootloader.

* __verilog.blink__ - The most basic verilog example. Blink a LED with gateware

## Amaranth examples
These example use Amaranth + Yosys, to synthesis (or compile) the Python based hardware description language into gateware. 
Amaranth will by default then automatically load the gateware onto the OrangeCrab using its DFU bootloader.

## Miscellaneous
If you are using a recent version of Ubuntu, you will not be able to access the dfu bootloader using normal permissions.
You can use the included udev rule `50-orangecrab.rules` to grant access to the orangecrab device to the `plugdev` group.

To install, type this command in a terminal:

```bash
$ sudo cp 50-orangecrab.rules /etc/udev/rules.d/50-orangecrab.rules
```

After this file is installed, physically unplug and reconnect the orangecrab device.

## RISC-V Cross Compiler Toolchain

To cross-compile for the bootloader's VexRiscv rv32i processor, you need a RISC-V compiler toolchain that includes support libraries for rv32i. Debian and Ubuntu currently have riscv64-unknown-elf compilers that will cross-compile for rv32i. But, to use those, you would need to build your own support libraries (libc, etc). For a ready-to-use option, you can download an embedded RISC-V toolchain from Embecosm's [Tool Chain Downloads](https://www.embecosm.com/resources/tool-chain-downloads/#riscv-stable) page.
