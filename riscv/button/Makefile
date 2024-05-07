
CROSS=riscv32-unknown-elf-
CFLAGS=

all: blink_fw.dfu

# ---- basic blink Target ----
dfu: blink_fw.dfu
	dfu-util -D blink_fw.dfu

# gcc13 needs -march=rv32i_zicsr (the old way was just -march=rv32i)
blink_fw.elf: start.s main.c
	$(CROSS)gcc $(CFLAGS) -march=rv32i_zicsr -mabi=ilp32 -Wl,-Bstatic,-T,sections.ld,--strip-debug -ffreestanding -nostdlib -I. -o blink_fw.elf start.s main.c

blink_fw.hex: blink_fw.elf
	$(CROSS)objcopy -O verilog blink_fw.elf blink_fw.hex

blink_fw.bin: blink_fw.elf
	$(CROSS)objcopy -O binary blink_fw.elf blink_fw.bin
	
blink_fw.dfu: blink_fw.bin
	cp blink_fw.bin blink_fw.dfu
	dfu-suffix -v 1209 -p 5bf0 -a blink_fw.dfu

# ---- 85F Target ----
dfu_85F: button_85F.dfu
	dfu-util -d 1209:5af0 --alt 0 -D button_85F.dfu | perl -ne 'print if $$n++>5'

button_85F.dfu: blink_fw.bin
	cp blink_fw.bin button_85F.dfu
	dfu-suffix -v 1209 -p 5af0 -a button_85F.dfu 2>&1 | perl -ne 'print if $$n++>5'

# ---- Clean ----

clean:
	rm -f blink_fw.bin blink_fw.elf blink_fw.dfu button_85F.dfu

.PHONY: all
