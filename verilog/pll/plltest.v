module plltest (
  input clk48,
  output rgb_led0_r,
  output rgb_led0_g,
  output rgb_led0_b
);

  // two 32-bit counters
  reg [31:0] counter1 = 0;
  reg [31:0] counter2 = 0;

  // counter1 is driven by the 48 MHz clock
  always @(posedge clk48) begin
    counter1 <= counter1 + 1;
  end

  // counter2 is driven by the 100 MHz PLL-generated clock
  always @(posedge clk100) begin
    counter2 <= counter2 + 1;
  end

  wire clk100;
  wire locked;

  // instantiate PLL
  pll my_pll(
    .clkin(clk48),
    .clkout0(clk100),
    .locked(locked)
  );

  // red is driven by counter1 divided by 2^27
  // green is driven by counter2 divided by 2^27
  // blue is driven by the PLL locked signal
  assign rgb_led0_r = counter1[26];
  assign rgb_led0_g = counter2[26];
  assign rgb_led0_b = ~locked;

endmodule
