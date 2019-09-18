import json
from pymemcache.client import base

import speech_recognition as sr 
from difflib import get_close_matches 
import threading

import serial

import time

import tkinter as tk

serialPort = serial.Serial(port = "/dev/ttyUSB0", baudrate=115200, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)

client = base.Client(('localhost', 11211))
shape_data_str = client.get('vision_data')

shape_data = json.loads(shape_data_str)

root = tk.Tk()
input_dat = tk.StringVar()

loca = [0,0]

print(shape_data)

color_pattern = ['blue', 'green', 'yellow', 'red']
action_pattern = ['pickup', 'drop', 'dance', 'grab']
obj_pattern = ['cube', 'square', 'cuboid', 'rectangle', 'triangle', 'prism', 'cone', 'hexagon', 'circle', 'sphere', 'ball' ]


def closeMatches(patterns, word):
	data = word.split()
	for temp in data: 
		match_list = get_close_matches(temp, patterns)
		if len(match_list) != 0:
			return match_list[0]
	return 1

def not_understood():
	print("Sorry, didn't understand that!")

def run():
    print(input_dat.get())
    instruction = input_dat.get()
    if (instruction != 1 or instruction != -1):
        action = closeMatches(action_pattern, instruction)
        if action != 1:
            print("Action: " + action)
        else:
            not_understood()
            return 0
        color = closeMatches(color_pattern, instruction)
        if color != 1:
            print("Color: " + color)
        else:
            not_understood()
            return 0
        obj = closeMatches(obj_pattern, instruction)
        if obj != 1:
            print("Object: " + obj)
            voice_dat = [action, color, obj]
            return voice_dat
        else:
            not_understood()
            return 0
    else:
        not_understood()
        return 0


def move():
    print("ACTIVE")
    voice_data = run()
    print(voice_data)
    if (voice_data != 0):
        if (voice_data[1] == "blue"):
            col = 0

        elif (voice_data[1] == "yellow"):
            col = 1

        elif (voice_data[1] == "red"):
            col = 2

        shape_data_str = client.get('vision_data')
        shape_data = json.loads(shape_data_str)
        loca[0] = shape_data[col][0][0]
        loca[1] = shape_data[col][0][1]
        if(shape_data[col][0][2] == voice_data[2]):
            while ( ( ( loca[0] >= ((600/2)+10) ) or ( loca[0] <= ((600/2)-10) ) ) ):
                print("Required Object at X:" + str(loca[0]) + " Y: " + str(loca[1]))
                shape_data_str = client.get('vision_data')
                shape_data = json.loads(shape_data_str)
                loca[0] = shape_data[col][0][0]
                loca[1] = shape_data[col][0][1]
                if (loca[0] <= ((600/2)+10)):
                    print("d")
                    serialPort.write(str.encode('d'))
                elif (loca[0] >= ((600/2)+10)):
                    print("a")
                    serialPort.write(str.encode('a'))
                time.sleep(0.1)

            while ( ( ( loca[1] >= ((480/2)+10) ) or ( loca[1] <= ((480/2)-10) ) ) ):
                print("Required Object at X:" + str(loca[0]) + " Y: " + str(loca[1]))
                shape_data_str = client.get('vision_data')
                shape_data = json.loads(shape_data_str)
                loca[0] = shape_data[col][0][0]
                loca[1] = shape_data[col][0][1]
                if (loca[1] <= ((480/2)+10)):
                    print("s")
                    serialPort.write(str.encode('s'))
                elif (loca[1] >= ((480/2)+10)):
                    print("w")
                    serialPort.write(str.encode('w'))
                time.sleep(0.1)
            test1=0

            while (serialPort.read().decode() != "s"):
                print("r")
                serialPort.write(str.encode('r'))
                time.sleep(0.1)

            while (test1 != 4):
                test1 = test1 + 1
                print("s")
                serialPort.write(str.encode('s'))
                time.sleep(0.1)

            serialPort.write(str.encode('c'))
            serialPort.flushInput()

            while (serialPort.read().decode() != "q"):
                print(serialPort.read().decode())
                serialPort.write(str.encode('f'))
                time.sleep(0.1)

            time.sleep(3)

            serialPort.write(str.encode('m'))


sbmitbtn = tk.Button(root, text = "Submit", command=lambda : move())
e1 = tk.Entry(root, textvariable=input_dat, width=80)
e1.pack()
sbmitbtn.pack()
root.mainloop()
exit()
