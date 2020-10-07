/* Copyright 2020 Gregory Davill <greg.davill@gmail.com> */
`default_nettype none

/*
 *  Blink a LED on the OrangeCrab using verilog
 */

module top (
    input CLK,
    output LED1,
    output LED2,
    output LED3
);
    // Create a 27 bit register
    reg [26:0] counter = 0;

    // Every positive edge increment register by 1
    always @(posedge CLK) begin
        counter <= counter + 1;
    end

    // Output inverted values of counter onto LEDs
    assign LED1 = ~counter[24];
    assign LED2 = ~counter[25];
    assign LED3 = 1;


endmodule