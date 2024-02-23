#!/usr/bin/env python3

import serial
import struct
import time
from crc32c import crc32c

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace 'COMx' with the appropriate port

def receiveData():
    while ser.in_waiting == 0:
        print("data not received!")
        time.sleep(1)
        pass
    receiveData = ser.read(4)
    receiveCRC = ser.read(4)

    # print(receiveData)
    # print(receiveCRC)

    return receiveData,receiveCRC

def check_crc(data, crc_received):
    # Calculate CRC for the received data
    crc_calculated = crc32c(data)
    print("---------------------------------")
    crc_ = struct.unpack('I', crc_received)
    # print(crc_calculated,crc_)
    # print(struct.unpack('I', crc_received)[0])

    # Compare calculated CRC with received CRC
    return crc_calculated == struct.unpack('I', crc_received)


if __name__ == "__main__":
    while True:
        data,crc = receiveData()
        time.sleep(1)
        if(check_crc(data,crc)):
            print("data matching")
        else:
            print("not matching")
            print("---------------------------------")

            
