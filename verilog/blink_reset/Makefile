PROJ=blink

# `r0.1` or `r0.2`
VERSION:=r0.2

all: ${PROJ}.dfu

dfu: ${PROJ}.dfu
	dfu-util -D $<


%.json: %.v
	yosys -p "synth_ecp5 -json $@" $<

%_out.config: %.json
	nextpnr-ecp5 --json $< --textcfg $@ --25k --package CSFBGA285 --lpf orangecrab_${VERSION}.pcf

%.bit: %_out.config
	ecppack --compress --freq 38.8 --input $< --bit $@

%.dfu : %.bit
	cp $< $@
	dfu-suffix -v 1209 -p 5af0 -a $@

clean:
	rm -f ${PROJ}.svf ${PROJ}.bit ${PROJ}.config ${PROJ}.json ${PROJ}.dfu 

.PHONY: prog clean
