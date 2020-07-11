/* Copyright 2020 Gregory Davill <greg.davill@gmail.com> */

/*  
 *  RISCV demo for the OrangeCrab Board.
 *   Press button to change colours on LED
 */


/* ---- Includes ---- */
#include <generated/csr.h>

/* ---- Function Prototypes ---- */
void msleep(int ms);
int button_active(void);
void write_rgb(uint8_t r, uint8_t g, uint8_t b);

/* ---- Main Function ---- */
int main() {

    /* This write turns off blink/rainbow modes */
    rgb_config_write(0x00);

    /* First read of this function may be invalid */
    button_active();

    int counter = 0;

    while(1){

        /* Wait for button press */
        while(button_active() == 0);

        /* Activate LED */
        if(counter == 0) write_rgb(0,  0,  255);
        if(counter == 1) write_rgb(0,  255,0  );
        if(counter == 2) write_rgb(255,0,  0  );

        /* Debounce counter */
        msleep(20);

        /* Count 0,1,2,0,1,2... */
        if(++counter > 2)
            counter = 0;
    }
    
    return 0;
}


/* ---- Helper Functions ---- */

/* ISRs will cause the CPU to jump here */
void isr() {

}

/* Simple sleep function that uses our timer0 peripheral */
void msleep(int ms)
{
    timer0_en_write(0);
    timer0_reload_write(0);
    timer0_load_write(CONFIG_CLOCK_FREQUENCY/1000*ms);
    timer0_en_write(1);
    timer0_update_value_write(1);
    while(timer0_value_read()) timer0_update_value_write(1);
}

/* Falling edge detector on the button */
int button_active(void){
    static int last_value = 1;

    int current_value = button_i_read();
    int button_activated = (last_value == 1) & (current_value == 0);
    last_value = current_value;

    return button_activated;
}

void write_rgb(uint8_t r, uint8_t g, uint8_t b){
    rgb__r_write(r);
    rgb__b_write(b);
    rgb__g_write(g);
}