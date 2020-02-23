
CROSS=riscv64-unknown-elf-
CFLAGS=

all: blink_fw.dfu

# ---- basic blink Target ----
dfu: blink_fw.dfu
	dfu-util -D blink_fw.dfu

blink_fw.elf: start.s main.c
	$(CROSS)gcc $(CFLAGS) -march=rv32im -mabi=ilp32 -Wl,-Bstatic,-T,sections.ld,--strip-debug -ffreestanding -nostdlib -I. -o blink_fw.elf start.s main.c

blink_fw.hex: blink_fw.elf
	$(CROSS)objcopy -O verilog blink_fw.elf blink_fw.hex

blink_fw.bin: blink_fw.elf
	$(CROSS)objcopy -O binary blink_fw.elf blink_fw.bin
	
blink_fw.dfu: blink_fw.bin
	cp blink_fw.bin blink_fw.dfu
	dfu-suffix -v 1209 -p 5bf0 -a blink_fw.dfu

# ---- Clean ----

clean:
	rm -f blink_fw.bin blink_fw.elf blink_fw.dfu

.PHONY: all