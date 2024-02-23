#!/usr/bin/env python3

import struct

# Packing multiple values into bytes
packed_data = struct.pack('>HHL', 123, 456, 789)  # Pack a short, a long, and another long in big-endian format
print("Packed Data:", packed_data)

# Unpacking bytes into multiple values
unpacked_values = struct.unpack('>HHL', packed_data)
print("Unpacked Values:", unpacked_values)


# Here the output:

# Packed Data: b'\x00{\x01\xc8\x00\x00\x03\x15'
# Unpacked Values: (123, 456, 789)