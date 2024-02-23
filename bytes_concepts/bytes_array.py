#!/usr/bin/env python3

import struct

# Example: Packing values into a bytearray
byte_array = bytearray()

# Pack an unsigned short, a float, and an integer into the bytearray
byte_array.extend(struct.pack('>Hfi', 123, 3.14, 42))

print("Packed Bytearray:", byte_array)

# Example: Unpacking values from a bytearray
# Unpack the values back from the bytearray
unpacked_values = struct.unpack('>Hfi', byte_array)

print("Unpacked Values:", unpacked_values)
