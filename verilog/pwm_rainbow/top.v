/* Copyright 2020 Gregory Davill <greg.davill@gmail.com>, 2020 Chris Marc Dailey (cmd) <nitz@users.noreply.github.com> */
`default_nettype none

/*
 *  Overview:
 *  The `top` module is responsable for stepping through
 *  the color wheel (255 color values representing steps
 *  through red, green, blue), and updating the PWM instances
 *  with duty cycles based on the current step.
 * 
 *  `top` also links the user button & rst_n to `orangecrab_reset`.
 */

module top (
	input clk48,

	output rgb_led0_r,
	output rgb_led0_g,
	output rgb_led0_b,

	output rst_n,
	input usr_btn
);
	// Create a 20 bit register for counting.
	// At 48 MHz, this counter will overflow at 100 Hz.
	reg [19:0] wheel_counter = 0;
	
	// An 8 bit value for the color wheel position register
	reg [7:0] wheel_position = 0;
	
	// 8 bit pwm duty-cycle registers, starting with blue full on.
	reg [7:0] pwm_dc_r = 0;
	reg [7:0] pwm_dc_g = 0;
	reg [7:0] pwm_dc_b = 255;
	
	// the pwm actives are wires, because
	// those values will come from modules
	wire pwm_active_r;
	wire pwm_active_g;
	wire pwm_active_b;
	
	// this wire will be used to control the reset module,
	// so that the board resets on the user button press.
	wire usr_btn_pressed = 0;

	always @(posedge clk48) begin
		wheel_counter <= wheel_counter + 1;
		
		// move wheel_position every time wheel_counter overflows.
		if (wheel_counter == 0)
			wheel_position <= wheel_position + 1;
		
		// update the rgb duty cycles based on wheel_position position
		if (wheel_position < 85) begin // blue down red up
			pwm_dc_r = (wheel_position*3);
			pwm_dc_g = 0;
			pwm_dc_b = 255 - (wheel_position*3);
		end else if (wheel_position < 170) begin // red down green up
			pwm_dc_r = 255 - ((wheel_position-85)*3);
			pwm_dc_g = ((wheel_position-85)*3);
			pwm_dc_b = 0;
		end else begin // green down blue up
			pwm_dc_r = 0;
			pwm_dc_g = 255 - ((wheel_position-170)*3);
			pwm_dc_b = ((wheel_position-170)*3);
		end
	end
	

	// output pwm values (high or low) onto LEDs
	// we use the inverted values from the pwm,
	// because the leds are active low.
	assign rgb_led0_r = ~pwm_active_r;
	assign rgb_led0_g = ~pwm_active_g;
	assign rgb_led0_b = ~pwm_active_b;
	
	// usr_btn is active low, so invert it for the reset module.
	assign usr_btn_pressed = ~usr_btn;

	// reset module instance
	orangecrab_reset reset(
		.clk(clk48), 
		.do_reset(usr_btn_pressed),  
		.nreset_out(rst_n)
	);

	// pwm instances, one for each color.
	pwm_8bit pwm_r(.clk(clk48), .reset(0), .duty_cycle(pwm_dc_r), .pwm_value(pwm_active_r));
	pwm_8bit pwm_g(.clk(clk48), .reset(0), .duty_cycle(pwm_dc_g), .pwm_value(pwm_active_g));
	pwm_8bit pwm_b(.clk(clk48), .reset(0), .duty_cycle(pwm_dc_b), .pwm_value(pwm_active_b));

endmodule
