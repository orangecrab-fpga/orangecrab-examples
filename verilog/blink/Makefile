PROJ=blink

all: ${PROJ}.dfu

dfu: ${PROJ}.dfu
	dfu-util -D $<


%.json: %.v
	yosys -p "synth_ecp5 -json $@" $<

%_out.config: %.json
	nextpnr-ecp5 --json $< --textcfg $@ --25k --package CSFBGA285 --lpf orangecrab_r0.2.pcf

%.bit: %_out.config
	ecppack --compress --freq 38.8 --spimode qspi --input $< --bit $@

%.dfu : %.bit
	cp $< $@
	dfu-suffix -v 1209 -p 5bf0 -a $@

clean:
	rm -f ${PROJ}.svf ${PROJ}.bit ${PROJ}.config ${PROJ}.json ${PROJ}.dfu 

.PHONY: prog clean
