#!/usr/bin/python3
# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports
import pyautogui

run = False
# Arduinoをデバイス名から検出
info_list = serial.tools.list_ports.comports()
for info in info_list:
    print(info.name)
    if 'usbmodem' in info.name: 
        run = True
        dev = "/dev/"+info.name
        
if run:
    ser = serial.Serial(dev)
    print(dev)
    while True:
        line = ser.readline()
        x, y, click = line.decode('shift-jis').split()
        pyautogui.moveRel(int(x), int(y))
        if int(click) == 1:
            pyautogui.click()
        if int(click) == 2:
            pyautogui.click(button="right")            
        print(x, y, click)
    ser.close()