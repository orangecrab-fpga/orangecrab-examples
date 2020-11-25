/* Copyright 2020 Chris Marc Dailey (cmd) <nitz@users.noreply.github.com> */
`default_nettype none

/*
 * A module that will reset OrangeCrab on input.
 */

module orangecrab_reset (
	input clk,
	input do_reset,
	output nreset_out
);
	// by default, we want the reset signal held high.
	reg reset_sr = 1'b1;
	
	always @(posedge clk) begin
		// if the do_reset signal ever goes high,
		// allow nreset_out to drop, resetting the board.
		if (do_reset)
			reset_sr <= 1'b0;
	end
	
	assign nreset_out = {reset_sr};

endmodule
