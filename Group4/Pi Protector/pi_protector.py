#!/usr/bin/env python
from MCP3008 import *
from Setup import *
import RPi.GPIO as GPIO

DEBUG = 0


# IR proximity sensor connected to adc #0
sensor_adc = 0

weAre = "Alec and Kendra"
print "hi " + weAre






        # read the analog pin
while True: 
	proximity = readadc(sensor_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
	if 600 >proximity > 300:
		print "too close! feel my wrath!"
		os.system("aplay diepie.wav")

		os.system("aplay piwarning.wav")
	elif proximity > 600:
		os.system("aplay roar.wav")
	print proximity



        # sleep for half a second
	time.sleep(0.5)