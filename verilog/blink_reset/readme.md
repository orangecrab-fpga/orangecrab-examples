# Blink Reset

## Overview
`blink_reset` is the sequel to the much acclaimed `blink` example. Almost identical, `blink_reset` adds one feature: resetting the OrangeCrab to bootloader mode on user button press.

## Files

- `blink_reset.v` — The `top` (e.g. 'main') module. Implements `blink` functionality, as well as handling the action of resetting the board by dropping the `rst_n` output low when `usr_btn` is pressed. (`usr_btn` is active low.)
- `Makefile` — The make build script that will produce the bitstream from the HDL.

## Pins/Physical Constraints File (.pcf)

You may be wondering how this module was able to add `usr_btn` and `rst_n` to it's inputs, and it just seemed to work. The physical constraints file (`../orangecrab_r0.(1|2).pcf`) describes the pins (e.g. physical constraints) of the FPGA device. In addition to tying names like `clk48` and `rst_n` to physical pins, it also sets their voltages, slew rates, IO types, pull modes, and more.

## Concepts Introduced

- Additional module (pins, in the case of the top module) inputs and outputs.
- Physical constraints file.
- Multiple always blocks.
- Fixed-width value assignment. (eg `1'b1`)

### Further Reading

- [fpga4fun: HDL Tutorials](https://www.fpga4fun.com/HDLtutorials.html) — Take a look at the Verilog section, as all of these examples use Verilog. VHDL, is another hardware description language that isn't used in these examples.
- [verilog_number_literals.pdf](http://web.engr.oregonstate.edu/~traylor/ece474/beamer_lectures/verilog_number_literals.pdf) — A few short slides that discuss number literals in Verilog. It covers bit width, signage, and radix. It also touches on unknown/high-z/don't care, which are not used in this example.