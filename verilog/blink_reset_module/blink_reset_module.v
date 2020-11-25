/* Copyright 2020 Gregory Davill <greg.davill@gmail.com>, 2020 Chris Marc Dailey (cmd) <nitz@users.noreply.github.com> */
`default_nettype none

/*
 *  Blink a LED on the OrangeCrab using verilog.
 *  Using a module, is able to reset the OrangeCrab by driving rst_n low.
 */

module top (
	input clk48,

	output rgb_led0_r,
	output rgb_led0_g,
	output rgb_led0_b,

	output rst_n,
	input usr_btn
);
	// Create a 27 bit register
	reg [26:0] counter = 0;
	
	// A 1-bit wire that will hold the inverse
	// of the user button value.
	wire user_button_pressed;

	// Every positive edge increment register by 1
	always @(posedge clk48) begin
		counter <= counter + 1;
	end

	// Output inverted values of counter onto LEDs
	assign rgb_led0_r = ~counter[24];
	assign rgb_led0_g = ~counter[25];
	assign rgb_led0_b = 1;

	// The user button pulls to ground when it's pressed, but 
	// the orangecrab_reset module expects logic 1
	// to pull it's reset wire low, so we will provide the inverse.
	assign user_button_pressed = ~usr_btn;

	orangecrab_reset reset_instance(
		.clk(clk48),
		.do_reset(user_button_pressed),
		.nreset_out(rst_n)
	);

endmodule

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

