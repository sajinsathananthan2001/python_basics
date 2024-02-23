#!/usr/bin/env python3

log_file = "/home/sajin/arduino_sampledata.txt" #where you have to mention the path where the datas to be stored

log_line = "the data that you need to store"

def logging_data(log_file, log_line):
    with open(log_file, 'a') as log:
        log.write(log_line + '\n')

