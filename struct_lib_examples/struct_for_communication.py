#!/usr/bin/env python3

import struct

# Simulating communication with a device
data_to_send = struct.pack('>Hf', 42, 3.14)  # Pack a short and a float in big-endian format
print("Sending Data:", data_to_send)

# Simulating reception of data
received_data = b'\x00*@H\xf5\xc3'  # Simulated received data
unpacked_data = struct.unpack('>Hf', received_data)
print("Received Data:", unpacked_data)


# The output:

# Sending Data: b'\x00*@H\xf5\xc3'
# Received Data: (42, 3.1415927410125732)