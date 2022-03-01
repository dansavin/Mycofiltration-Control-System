#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for testing Arduino-RaspberryPi serial communication.

Arduino prints lines of comma-separated data to a serial port.
This script reads user-fixed amount of entries from the serial port.
Each entry is formatted, timestamped, and appended to a .csv file.
"""

import serial
import datetime
import csv

# info
__author__ = "Daniel Savin"
__email__ = "dansavin11@gmail.com"
__version__ = "1.0.0"

# variables
port = 'COM3'
bauds = 9600
filename = 'dump.csv'
numberOfReadings = 5


def write_from_arduino():
    # main body runs until a certain amount of readings is reached
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        with serial.Serial(port, bauds) as arduino:
            for x in range(numberOfReadings):
                arduino_rx = str(arduino.readline())  # read serial from arduino
                data = arduino_rx[2:len(arduino_rx)-5]  # remove header
                data_list = data.split(",")  # split data by comma into entries
                timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')  # get current date and time
                data_list.insert(0, timestamp)  # add a timestamp
                writer.writerow(data_list)  # write resulting array to .csv file
        csvfile.close()  # close the file


if __name__ == '__main__':
    write_from_arduino()
