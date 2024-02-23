#!/usr/bin/env python3


import struct

# Packing values into bytes
packed_data = struct.pack('>I', 42432)  # Pack an unsigned integer (4 bytes) in big-endian format, Here the 42432 is a random number 
print("Packed Data:", packed_data)

# Unpacking bytes into values
unpacked_value = struct.unpack('>I', packed_data)
print("Unpacked Value:", unpacked_value[0])



# Output of Packing and Unpacking:

# Packed Data: b'\x00\x00\xa5\xc0'
# Unpacked Value: 42432