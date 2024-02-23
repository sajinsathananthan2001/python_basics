#!/usr/bin/env python3
import serial
import struct

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace 'COMx' with the appropriate port

def receive_data():
    # Wait until data is available
    while ser.in_waiting == 0:
        pass

    # Receive the data
    received_data = ser.read(4)  # Assuming data size is 4 bytes
    received_crc = ser.read(2)  # Assuming CRC size is 2 bytes

    return received_data, received_crc

def check_crc(data, crc_received):
    # Calculate CRC for the received data
    crc_calculated = calculate_crc(data)

    # Compare calculated CRC with received CRC
    return crc_calculated == struct.unpack('H', crc_received)[0]

def calculate_crc(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc = crc >> 1
    return crc

while True:
    data, crc = receive_data()

    if check_crc(data, crc):
        print("CRC Matched!")
        print("Received Data:", data)
    else:
        print("CRC Mismatch! Discarding Data.")
