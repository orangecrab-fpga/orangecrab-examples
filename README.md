# OrangeCrab example projects
This repository contains example code to be run on the OrangeCrab.

---

## RISCV examples
    These examples make use of the Vexriscv CPU created inside the FPGA by the bootloader. The RISCV firmware is copied across into the FLASH by the bootloader. If the bootloader determines that it has not loaded new gateware, then the CPU will simply adjust it's program counter to start executing the newly loaded programs.

### riscv.blink
The most basic example. It blinks a LED 