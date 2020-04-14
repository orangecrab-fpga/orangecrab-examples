#!/usr/bin/env python3

import argparse
import os
import struct
import binascii


flash_regions_final = {
#                                                         "0x00000000", # Bootloader
    "soc_basesoc_orangecrab/gateware/ecp_bitstream.bit":  "0x00080000", # SoC ECP5 Bitstream
    "firmware.bin":                                       "0x00140000", # Circuit PYthon
}

flash_regions = {}

offset = int("0x00080000", 16)
for filename, base in flash_regions_final.items():
    base = int(base, 16)
    new_address = base - offset
    print(f'Moving {filename} from 0x{base:08x} to 0x{new_address:08x}')
    flash_regions[filename] = new_address


output_file = 'combine.dfu'
total_len = 0
with open(output_file, "wb") as f:
    for filename, base in flash_regions.items():
        data = open(filename, "rb").read()
        crc = binascii.crc32(data)
        
        print(f' ')
        print(f'Inserting {filename:60}')
        print(f'  Start address: 0x{base + offset:08x}')
        
        data_write = bytearray()
        if(total_len != 0):
            data_write += struct.pack('<I', len(data)) # len
            data_write += struct.pack('<I', crc) # CRC
            print(f'  Length       : 0x{len(data):08x} bytes')
            print(f'  crc32        : 0x{crc:08x}')
        data_write += data
        print(f'           data: ' + f' '.join(f'{i:02x}' for i in data_write[:16]))
        f.seek(base)
        f.write(data_write)

        total_len += len(data_write)

os.system(f"dfu-suffix -v 1209 -p 5bf0 -a {output_file}")
