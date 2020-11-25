/* Copyright 2020 Chris Marc Dailey (cmd) <nitz@users.noreply.github.com> */
`default_nettype none

/*
 *  A simple 8-bit PWM.
 *
 *  On clock pulses, a counter will increment, and
 *  it's value be compared to the duty_cycle. If 
 *  the counter is less than the duty_cycle, the 
 *  output value will be high, otherwise low.
 *
 *  When the 8-bit counter overflows, the cycle restarts.
 *  A duty_cycle of 0 will also reset the counter.
 */

module pwm_8bit (
	input clk,
	input reset,
	input [7:0] duty_cycle,
	output pwm_value
);
	// 8-bit counter for the pwm period.
	wire [7:0] counter_val;
	
	// If the user asks or DC is 0, reset the counter.
	// This is an implicit continuous assignment,
	// equivilant to:
	// wire should_reset;
	// assign should_reset = (reset || duty_cycle == 0);
	wire should_reset = reset || (duty_cycle == 0);
	
	// if our counter is under our dc value,
	// set output high, otherwise low.
	assign pwm_value = (duty_cycle > counter_val) ? 1 : 0;
	
	// counter instance for counting the period
	counter_8bit period_counter(
		.clk(clk),
		.out_value(counter_val),
		.reset(should_reset)
	);

endmodule
