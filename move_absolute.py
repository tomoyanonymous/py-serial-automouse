#!/usr/bin/python3

# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports
import pyautogui

nano = False
info_list = serial.tools.list_ports.comports()

for info in info_list:
    print(info.name)
    if 'usbmodem' in info.name: 
        nano = True
        dev = "/dev/"+info.name
w,h = pyautogui.size();

if nano:
    ser = serial.Serial(dev)
    print(dev)
    while True:
        line = ser.readline()
        x, y, click= line.decode('shift-jis').split()
        x_abs = float(x)*float(w)/1024.0;
        y_abs = float(y)*float(h)/1024.0;
        pyautogui.moveTo(int(x_abs), int(y_abs),duration=0.05)
        if int(click) == 1:
            pyautogui.click()
        if int(click) == 2:
            pyautogui.click(button="right")            
        print(x, y, click)
    ser.close()
