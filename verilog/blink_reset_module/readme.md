# Blink Reset (Module)

## Overview
`blink_reset_module` has the same functionality as `blink_reset`. It however moves the reset logic into a module named `orangecrab_reset`. `orangecrab_reset` checks it's input named `do_reset` to decide when to allow it's `nreset_out` output to be driven low. The module `top` instantiates an `orangecrab_reset`, and connects it's `rst_n` wire, as well as a wire representing the negation of the `usr_btn` input. 

## Files

- `blink_reset_module.v` — The `top`, implemening `blink` functionality, and connecting wires to the `orangecrab_reset` module, defined below it.
- `Makefile` — The make build script that will produce the bitstream from the HDL.

## Concepts Introduced

- Multiple modules, and instantiating a sub-level modules.
- Wire connections to other modules.

### Further Reading

- [Stack Overflow: Verilog: How to instantiate a module](https://stackoverflow.com/a/20066851/944605) — A refreshingly thorough yet brief explanation of module instantiating.
- [Introduction to Combinational Verilog](http://www.eecs.umich.edu/courses/eecs270/270lab/270_docs/intro_verilog.pdf) — Slides from a Univeristy of Michigan lab document that goes over how modules can be used to organize logic. 