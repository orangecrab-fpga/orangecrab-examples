/* Copyright 2020 Gregory Davill <greg.davill@gmail.com> */

/*
 *  Blink a LED on the OrangeCrab using verilog
 */

module top (
    input CLK,

	output LED1,
	output LED2,
	output LED3,

	output RST_N,
	input BTN_N
);
    reg [26:0] counter = 0;

	always @(posedge CLK) begin
		counter <= counter + 1;
	end

	assign LED1 = ~counter[24];
    assign LED2 = ~counter[25];
    assign LED3 = 1;

	/* Reset logic on button press */
	reg reset_sr = 1'b1;
	always @(posedge CLK) begin
		reset_sr <= {BTN_N};
	end
	assign RST_N = reset_sr;
    

endmodule