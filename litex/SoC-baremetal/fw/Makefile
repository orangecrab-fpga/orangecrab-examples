include ../include/generated/variables.mak
include $(SOC_DIRECTORY)/software/common.mak

CFLAGS += -fpack-struct -O3

OBJECTS=main.o isr.o

all: oc-fw.bin size

%.bin: %.elf
	$(OBJCOPY) -O binary $< $@
ifneq ($(OS),Windows_NT)
	chmod -x $@
endif
ifeq ($(CPUENDIANNESS),little)
	$(PYTHON) -m litex.soc.software.mkmscimg $@ --little
else
	$(PYTHON) -m litex.soc.software.mkmscimg $@
endif

oc-fw.elf: $(FW_DIRECTORY)/linker.ld $(OBJECTS)

%.elf: 
	$(LD) $(LDFLAGS) -L$(BUILDINC_DIRECTORY)/generated -T $(FW_DIRECTORY)/linker.ld -N -o $@ \
		../libbase/crt0-$(CPU)-ctr.o \
		$(OBJECTS) \
		-L../libbase \
		-L../libcompiler_rt \
		-lbase-nofloat -lcompiler_rt
ifneq ($(OS),Windows_NT)
	chmod -x $@
endif

# pull in dependency info for *existing* .o files
-include $(OBJECTS:.o=.d)

%.o: $(FW_DIRECTORY)/%.c
	$(compile)

%.o: $(FW_DIRECTORY)/%.S
	$(assemble)

clean:
	$(RM) $(OBJECTS) oc-fw.elf oc-fw.bin .*~ *~

size:
	$(TARGET_PREFIX)size oc-fw.elf


.PHONY: all clean
