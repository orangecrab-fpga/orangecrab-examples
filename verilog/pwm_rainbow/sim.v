/* Copyright 2020 Chris Marc Dailey (cmd) <nitz@users.noreply.github.com> */
`default_nettype none

/*
 *  A small simulation test harness.
 */

module sim (
	input clk,
	output r,
	output g,
	output b,
	output rst
);
	reg btn = 0;
	top sim_top(clk, r, g, b, rst, btn);
endmodule
