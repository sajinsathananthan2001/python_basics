#!/usr/bin/env python3

import serial
import struct
from crc32c import crc32c

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace 'COMx' with the appropriate port

def receive_data():
    # Wait until data is available
    while ser.in_waiting == 0:
        pass

    # Receive the data
    received_data = ser.read(4)  # Assuming data size is 4 bytes
    received_crc = ser.read(4)

    return received_data, received_crc

def check_crc(data, crc_received):
    # Calculate CRC for the received data
    crc_calculated = crc32c(data)

    # Compare calculated CRC with received CRC
    return crc_calculated == struct.unpack('I', crc_received)[0]

while True:
    data, crc = receive_data()

    if check_crc(data, crc):
        print("CRC Matched!")
        print("Received Data:", data)
    else:
        print("CRC Mismatch! Discarding Data.")
