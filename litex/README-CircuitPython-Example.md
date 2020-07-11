# OrangeCrab DDR3 SoC CircuitPython demo

``` Currently under-development ``` 

## Build Instructions
```console
$ python3 SoC-CircuitPython.py
 ```
If this is the first time running this command it will pull in submodules of LiteX and all the dependancies requiled to build. Then this will invoke LiteX/Migen to generate verilog and fed it to yosys/nextpnr to generate a bitstream for the ECP5.

When the synthesis is complete you will find the gateware to be loaded at `"build/orangecrab/gateware/orangecrab.bit"`

## Compile CircuitPython
```console
$ git clone https://github.com/gregdavill/circuitpython.git -b orangecrab
$ cd circuitpython 
$ git submodule update --init --recursive
$ cd ports/litex
$ make BOARD=orangecrab
```

## Combine SoC and Circuit Python firmware and flash
Copy `circuitpython/ports/litex/build-orangecrab/firmware.bin` into this directory, and use this command to create a combined binary.
This step creates a single binary that will fit our code at `0x80000`, and CircuitPython riscv code at `0x100000` in FLASH after we've loaded it through the DFU bootloader.
 ```console
$ python combine.py
$ dfu-util -D combine.dfu
 ```

## CircuitPython is now running!

If you run dmesg, you shloud see a new ttyACM0 attached, as well as a Mass storage device
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
Adafruit CircuitPython 5.2.0-24-gc88db8a4e-dirty on 2020-07-11; OrangeCrab with VexRiscv
>>> 
```