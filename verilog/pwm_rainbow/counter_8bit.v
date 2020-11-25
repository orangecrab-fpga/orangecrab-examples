/* Copyright 2020 Chris Marc Dailey (cmd) <nitz@users.noreply.github.com> */
`default_nettype none

/*
 * An 8-bit counter.
 */

module counter_8bit (
	input clk,
	input reset,
	output reg [7:0] out_value
);
	always @(posedge clk)
		if (reset)
			out_value <= 8'b0;
		else
			out_value <= out_value + 1;
endmodule
