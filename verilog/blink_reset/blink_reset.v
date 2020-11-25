/* Copyright 2020 Gregory Davill <greg.davill@gmail.com> */
`default_nettype none

/*
 *  Blink a LED on the OrangeCrab using verilog
 *  Is able to reset the OrangeCrab by driving rst_n low on btn0 press.
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

    // Every positive edge increment register by 1
    always @(posedge clk48) begin
        counter <= counter + 1;
    end

    // Output inverted values of counter onto LEDs
    assign rgb_led0_r = ~counter[24];
    assign rgb_led0_g = ~counter[25];
    assign rgb_led0_b = 1;

    // Reset logic on button press.
    // this will enter the bootloader
    reg reset_sr = 1'b1;
    always @(posedge clk48) begin
        reset_sr <= {usr_btn};
    end
    assign rst_n = reset_sr;


endmodule
