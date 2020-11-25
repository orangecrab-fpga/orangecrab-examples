# Verilog Examples

## Overview
This directory contains Verilog HDL examples. If you're just getting started, take a look at the `blink` example, 

These examples use Yosys + NextPnR, to synthesis (or compile) verilog into a bitstream. A nice term for this is gateware. Since it is analogous to firmware, but describes how the FPGA needs to be configured.

This gateware can be loaded onto the OrangeCrab using its DFU bootloader.

To build the gateware for an example, run `make` in it's directory. If you're ready to load the gateware to your OrangeCrab, run `make dfu`. Your OrangeCrab will need to be in bootloader mode to accept the gateware. Boot it into bootloader mode by powering it on while holding down [[btn0]].

## Examples

 - `blink` — The first thing you do with any new board! Make the LED blink, with gateware!
 - `blink_reset` — As above, but with a bonus! When the [[btn0]] is pressed, OrangeCrab will reset into the bootloader mode.