# OrangeCrab DDR3 SoC CircuitPython demo

``` Currently under-development ``` 

## Build Instructions
Use the --device flag if you have a non-standard ECP5 fitted 
```console
$ python3 OrangeCrab-bitstream.py [--device 85F]
 ```

Right now I'm missing proper 5G support in the platform file, so use these commands if you have a 5G-85F part fitted.
```console
$ ecppack --spimode qspi --freq 38.8 --compress --idcode 0x81113043 --input soc_basesoc_orangecrab/gateware/top.config --bit soc_basesoc_orangecrab/gateware/ecp_bitstream.bit
```

This will invoke Litex/Migen to create a verilog file, this is then fed to yosys/nextpnr to generate a bitstream for the ECP5.
When the synthesis is complete you will find the gateware to be loaded at "soc_basesoc_orangecrab/gateware/ecp_bitstream.bit"

## Compile CircuitPython
```console
$ git clone https://github.com/gregdavill/circuitpython.git -b orangecrab
$ cd circuitpython 
$ git submodule update --init --recursive
$ cd ports/litex
$ make BOARD=orangecrab
```

## Adding CircuitPython binary
copy `circuitpython/ports/litex/build-orangecrab/firmware.bin` into this directory, acnd use this command to create a combined binary.
 ```console
$ python combine.py
 ```


This now loads our new SoC into FLASH at `0x80000`, and CircuitPython riscv code at `0x140000`
## Flash to board
```console
$ dfu-util -D combine.dfu
```

## If required watch the BIOS run
Connect a serial link to the OrangeCrab on its external pins TX=0, RX=1

In a new terminal run the litex_term (Or another Serial terminal such as screen), reload the bitstream to see this splash screen.
```console
$ litex_term --speed 115200 [port]
[LXTERM] Starting....
        __   _ __      _  __
       / /  (_) /____ | |/_/
      / /__/ / __/ -_)>  <
     /____/_/\__/\__/_/|_|
   Build your hardware, easily!

 (c) Copyright 2012-2020 Enjoy-Digital
 (c) Copyright 2007-2015 M-Labs

 BIOS built on Apr 14 2020 21:30:01
 BIOS CRC passed (fee74f97)

 Migen git sha1: e2e6c72
 LiteX git sha1: 91981b96

--=============== SoC ==================--
CPU:       VexRiscv @ 48MHz
ROM:       32KB
SRAM:      4KB
L2:        8KB
MAIN-RAM:  131072KB

--========== Initialization ============--
Initializing SDRAM...
SDRAM now under software control
Read leveling:
m0, b0: |00001110| delays: 05+-01
best: m0, b0 delays: 05+-01
m1, b0: |00001110| delays: 05+-01
best: m1, b0 delays: 05+-01
SDRAM now under hardware control
Memtest OK
Memspeed Writes: 82Mbps Reads: 131Mbps

--============== Boot ==================--
Booting from serial...
Press Q or ESC to abort boot completely.
sL5DdSMmkekro
Timeout
Booting from flash...
Loading 294312 bytes from flash...
Executing booted program at 0x40000000

--============= Liftoff! ===============--
```

## CircuitPython

If you run dmesg, you shloudu see a new ttyACM0 attached, as well as a Mass storage device
```console
$ dmesg
[3660.128564] usb 1-1: new full-speed USB device number 85 using xhci_hcd
[3660.303067] usb 1-1: New USB device found, idVendor=1209, idProduct=5bf0
[3660.303076] usb 1-1: New USB device strings: Mfr=2, Product=3, SerialNumber=1
[3660.303081] usb 1-1: Product: OrangeCrab
[3660.303086] usb 1-1: Manufacturer: GsD
[3660.303090] usb 1-1: SerialNumber: 4E96033DB132B362
[3660.308700] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
[3660.316766] usb-storage 1-1:1.2: USB Mass Storage device detected
[3660.317336] scsi host4: usb-storage 1-1:1.2
[3660.332957] input: GsD OrangeCrab as /devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1:1.3/0003:1209:5BF0.008D/input/input186
[3660.393971] hid-generic 0003:1209:5BF0.008D: input,hidraw5: USB HID v1.11 Keyboard [GsD OrangeCrab] on usb-0000:00:14.0-1/input3
[3661.337027] scsi host4: scsi scan: INQUIRY result too short (5), using 36
[3661.337041] scsi 4:0:0:0: Direct-Access     GsD      OrangeCrab       1.0  PQ: 0 ANSI: 2
[3661.338035] sd 4:0:0:0: Attached scsi generic sg2 type 0
[3661.345245] sd 4:0:0:0: [sdc] 16385 512-byte logical blocks: (8.39 MB/8.00 MiB)
[3661.349456] sd 4:0:0:0: [sdc] Write Protect is off
[3661.349470] sd 4:0:0:0: [sdc] Mode Sense: 03 00 00 00
[3661.353458] sd 4:0:0:0: [sdc] No Caching mode page found
[3661.353471] sd 4:0:0:0: [sdc] Assuming drive cache: write through
[3661.418044]  sdc: sdc1
[3661.444235] sd 4:0:0:0: [sdc] Attached SCSI removable disk
```

Connecting to the ttyACM0 device you should see the following
```console
$ screen /dev/ttyACM0
Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.

Press any key to enter the REPL. Use CTRL-D to reload.
Adafruit CircuitPython 5.2.0-24-gc88db8a4e-dirty on 2020-04-14; OrangeCrab with VexRiscv
>>> 
```