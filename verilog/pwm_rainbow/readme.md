# PWM Rainbow

## Overview

PWM Rainbow is an advanced blinky example. Instead of just turning on some of the colors of the RGB LED, PWM rainbow adds a bit more functionality and complexity. PWM Rainbow will, as it's name implies, use a pulse width modulation strategy to vary the intensity of the RGB LED. As well, it will cycle through a nice rainbow of colors from red, to green, to blue, then back to red, repeating infinitely.

Upon first seeing it, it seems like the LED might be behaving as if the OrangeCrab were in bootloader mode. Look closer, and you'll notice a difference in direction and intensity of how the colors fade. As well, pressing [[btn0]] will reset the board to the bootloader, so you can see the difference immediately!

This example builds on the example `blink_reset_module`. Take a look at it if you're looking for a smaller example that introduces modules.

## Files

- `top.v` — The `top` module, responsable for counting through the color wheel, and hooking the pwm outputs to the LED(s).
- `orangecrab_reset.v` — The `orangecrab_reset` module, which sets an output wire low when it's input is high on a clock edge.
- `counter_8bit.v` — An 8 bit counter module, used by the PWM module as it's period.
- `pwm_8bit.v` — An 8 bit PWM module that accepts a varying duty cycle.
- `Makefile` — The make build script that will produce the bitstream from the HDL. The makefile has been modified considerably from previous examples.

## Makefile Changes

To this point, the Makefile in each example has been a very simple example of the `yosys`/`nextpnr`/`ecppack` tool flow. This example has a slightly more advanced usage of `yosys`. Some of the changes are explained here, but be sure to check the comments in the Makefile itself for more information.

#### Multiple Verilog Files

Each module is seperated into it's own .v file. The Makefile accounts for this, by using the `$(wildcard)` funtion to collect the names of all .v files in this directory.

#### Yosys Invocation

Instead of the one-line `yosys -p` invocation to just run it's `synth_ecp5` command, instead we are building a yosys script with several commands. The script, built in the `%.ys` recipe, creates a temporary file that contains those commands.

First, the file will contain a `read_verilog` command for each .v file in the directory. Then, it will have the `synth_ecp5` command, specifying the top module as defined by the `TOP_MODULE` variable. Lastly, it will write out the json file that `nextpnr` expects, by using the `write_json` command.

The temporary script will look like this:

```
read_verilog counter_8bit.v
read_verilog orangecrab_reset.v
read_verilog pwm_8bit.v
read_verilog sim.v
read_verilog top.v
synth_ecp5 -top top
write_json pwm_rainbow.json
```

That script will be used by the command `yosys -s`, executing each of those commands in order.

#### Simulation

> *Note: Requires [gtkwave](https://sourceforge.net/projects/gtkwave/) on your path.*

Another makefile target, `sim` has also been added. `sim` will use the same method of generating a `.ys` script, except rather than calling `synth_ecp5` and `write_json`, the script will instead call other commands.

First, `prep -top sim`. `prep` is a precursor command that normally occurs implicitly in `synth_ecp5`. We are explicitly invoked to set the top module to `sim`, defined in `sim.v`. The `sim` module acts as our test harness, creating a top module inside it.

Then, the `sim` command is invoked with a few paramaters:

- `-clock clk` — Tells the sim command to use the net named `clk` as the net to supply simulation clock pulses to.
- `-n $(SIMULATION_CYCLES)` — The number of clock cycles (full pulses) to simulate.
- `-vcd $(basename $@).vcd` — Tells the sim command to output a file named pwm_rainbow.vcd.

The `sim` command will take while to complete the simulation cycles.

The vcd file is then passed to `gtkwave` to be viewed.

## Concepts Introduced

- Multiple modules, split into multiple files.
- Yosys scripting.
- A simple PWM.
- Implicit continuous assignment (in `pwm_8bit.v`)
- Simple simulation.

### Further Reading

- [fpga4fun: PWM & DAC](https://www.fpga4fun.com/PWM_DAC.html)