#!/usr/bin/env python3

import struct

# Packing and unpacking mixed data types
mixed_data = struct.pack('>cHd', b'A', 123, 3.14)  # Pack a char, a short, and a double in big-endian format
print("Mixed Data:", mixed_data)

unpacked_mixed = struct.unpack('>cHd', mixed_data)
print("Unpacked Mixed Data:", unpacked_mixed)
