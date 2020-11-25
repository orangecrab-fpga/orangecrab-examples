# Blink

## Overview
`blink` is the hello world of any development board: Make the LED blink! A singular Verilog file describes a module that increments a 27 bit counter. That counter increments on every positive colock edge. It uses the second and third highest bit to turn on the red and green colors of the RGB LED. You'll see the LED show red, then green, then both before turning off and re-starting the sequence as the counter continues to overflow.

## Files

- `blink.v` — The `top` (e.g. 'main') module, that describes the counter, and the hooking of the counter's bits to the RGB LED.
- `Makefile` — The make build script that will produce the bitstream from the HDL. It makes uses of the open source tools `yosys`, `nextpnr`, `ecppack`, and `dfu-util` to go from hardware description to bitstream to running on the FPGA.

## Concepts Introduced

- Simple toolchain flow via Makefile
- Introduction to Verilog HDL.
- Registers and assignment, always blocks, sequential logic.
- Wire assignment (combinitorial logic)

### Further Reading

- [fpga4fun: Counters 1 - Binary counters](https://www.fpga4fun.com/Counters1.html) — A more in detph look at how the counting is done like in this example.
- [fpga4fun: HDL Tutorials](https://www.fpga4fun.com/HDLtutorials.html) — Take a look at the Verilog section, as all of these examples use Verilog. VHDL, is another hardware description language that isn't used in these examples.
