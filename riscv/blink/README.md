# riscv.blink
It blinks the LED

## Building & Loading
1. Generate a riscv binary and create a dfu update image.
```console
$ make all
```

2. Enter the DFU bootloader by holding the button while connecting OrangeCrab to your USB port

3. You can validate that the OrangeCrab is in DFU mode using `dmesg`
```
    usb 1-1: new full-speed USB device number 63 using xhci_hcd
    usb 1-1: New USB device found, idVendor=1209, idProduct=5bf0
    usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
    usb 1-1: Product: OrangeCrab r0.2 DFU Bootloader v2.0.3-13-g84c820a
    usb 1-1: Manufacturer: GsD
```

4. Load the RISCV firmware we've just built using
```console
$ make dfu
```