PROJ=usb_acm_device
TOP_MODULE=usb_acm_device

# Specify hardware revision of your OrangeCrab: `r0.1` or `r0.2` or `r0.2.1`
VERSION:=r0.2.1
# `25F` or `85F`
DENSITY=25F

ifneq (,$(findstring 85,$(DENSITY)))
	NEXTPNR_DENSITY:=--85k
else
	NEXTPNR_DENSITY:=--25k
endif

# By default, we will read all verilog files (.v) in this directory.
RTL_USB_DIR=blocks/usbserial/usb
VERILOG_FILES=$(RTL_USB_DIR)/edge_detect.v \
	$(RTL_USB_DIR)/serial.v \
	$(RTL_USB_DIR)/usb_fs_in_arb.v \
	$(RTL_USB_DIR)/usb_fs_in_pe.v \
	$(RTL_USB_DIR)/usb_fs_out_arb.v \
	$(RTL_USB_DIR)/usb_fs_out_pe.v \
	$(RTL_USB_DIR)/usb_fs_pe.v \
	$(RTL_USB_DIR)/usb_fs_rx.v \
	$(RTL_USB_DIR)/usb_fs_tx_mux.v \
	$(RTL_USB_DIR)/usb_fs_tx.v \
	$(RTL_USB_DIR)/usb_reset_det.v \
	$(RTL_USB_DIR)/usb_serial_ctrl_ep.v \
	$(RTL_USB_DIR)/usb_uart_bridge_ep.v \
	$(RTL_USB_DIR)/usb_uart_core.v \
	usb_acm_device.v

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

all: $(PROJ).dfu

dfu: $(PROJ).dfu
	dfu-util --alt 0 -D $<
	
# We don't actually need to do anything to verilog files.
# This explicitly empty recipe is merely referenced from
# the %.ys recipe below. Since it depends on those files,
# make will check them for modifications to know if it needs to rebuild.
%.v: ;

# Build the yosys script.
# This recipe depends on the actual verilog files (defined in $(VERILOG_FILES))
# Also, this recipe will generate the whole script as an intermediate file.
# The script will call read_verilog for each file listed in $(VERILOG_FILES),
# Then, the script will execute synth_ecp5, looking for the top module named $(TOP_MODULE)
# Lastly, it will write the json output for nextpnr-ecp5 to use as input.
%.ys: $(VERILOG_FILES)
	$(file >$@)
	$(foreach V,$(VERILOG_FILES),$(file >>$@,read_verilog $V))
	$(file >>$@,synth_ecp5 -top $(TOP_MODULE)) \
	$(file >>$@,write_json "$(basename $@).json") \
	
	
# Run the yosys script to synthasize the logic and netlist (in json format)
# to provide for nextpnr-ecp5.
%.json: %.ys
	yosys -s "$<"

# Run nextpnr-ecp5 to place the logic components and route the nets to pins.
%_out.config: %.json
	nextpnr-ecp5 --json $< --textcfg $@ $(NEXTPNR_DENSITY) --package CSFBGA285 --lpf ..$(PATH_SEP)orangecrab_${VERSION}.pcf

# Generate the final bitstream from the pnr output.
%.bit: %_out.config
	ecppack --compress --freq 38.8 --input $< --bit $@

# Add OrangeCrab's USB VID/PID to the bitstream, so it's ready for DFU xfer to the bootloader.
%.dfu : %.bit
	$(COPY) $< $@
	dfu-suffix -v 1209 -p 5af0 -a $@

clean:
	$(RM) -f $(PROJ).svf $(PROJ).bit $(PROJ)_out.config $(PROJ).json $(PROJ).dfu $(PROJ).vcd

.PHONY: sim clean
