# riscv.button
Read input from button, toggle through colours on the LED


## Dependencies

Assuming you are using Ubuntu or Debian Linux, you will need:

1. `riscv-unknown-elf` cross compiler (see [../../README.md](../../README.md))

2. udev rule allowing read and write permissions for your OrangeCrab 25F or
   85F (see [../../README.md](../../README.md))

3. `dfu-util` (you can install with `sudo apt install dfu-util`)


## Building & Loading for OrangeCrab 85F with gcc 13

1. Generate a riscv binary and create a dfu update image:
   ```console
   $ make button_85F.dfu
   ```
2. Make sure the OrangeCrab 85F is in DFU mode by plugging in the USB cable
   while holding down the button. You can check for a DFU device with `lsusb`
   or `dmseg`. You may need to add a udev rule to give the `plugdev` group
   permissions for `1209:5af0` if you have not already done so. You also need
   to have `dfu-util` installed (e.g. `sudo apt install dfu-util`).

3. Load the new firmware into the `-d 1209:5af0 --alt 0` DFU device with
   ```console
   $ make dfu_85F
   ```

## Building & Loading for OrangeCrab 25F
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
