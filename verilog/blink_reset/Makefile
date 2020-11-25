PROJ=blink_reset

# `r0.1` or `r0.2`
VERSION:=r0.2

# Add Windows and Unix support
RM         = rm -rf
COPY       = cp -a
PATH_SEP   = /
ifeq ($(OS),Windows_NT)
# When SHELL=sh.exe and this actually exists, make will silently
# switch to using that instead of cmd.exe.  Unfortunately, there's
# no way to tell which environment we're running under without either
# (1) printing out an error message, or (2) finding something that
# works everywhere.
# As a result, we force the shell to be cmd.exe, so it works both
# under cygwin and normal Windows.
SHELL      = cmd.exe
COPY       = copy
RM         = del
PATH_SEP   = \\
endif


all: ${PROJ}.dfu

dfu: ${PROJ}.dfu
	dfu-util -D $<


%.json: %.v
	yosys -p "synth_ecp5 -json $@" $<

%_out.config: %.json
	nextpnr-ecp5 --json $< --textcfg $@ --25k --package CSFBGA285 --lpf ..$(PATH_SEP)orangecrab_${VERSION}.pcf

%.bit: %_out.config
	ecppack --compress --freq 38.8 --input $< --bit $@

%.dfu : %.bit
	$(COPY) $< $@
	dfu-suffix -v 1209 -p 5af0 -a $@

clean:
	$(RM) -f ${PROJ}.svf ${PROJ}.bit ${PROJ}.config ${PROJ}.json ${PROJ}.dfu 

.PHONY: prog clean
