#!/usr/bin/env python
from MCP3008 import *
from Setup import *
import RPi.GPIO as GPIO

DEBUG = 0

# IR proximity sensor connected to adc #0
sensor_adc = 0


#--------------------------

print "hi"




while True:
        # read the analog pin
        proximity = readadc(sensor_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
	print proximity


	if proximity > 524:
		os.system("aplay Group\ 3.wav")
	if  300 < proximity < 524:
		os.system ("aplay Group3a.wav")

	



        # sleep for half a second
        time.sleep(0.5)
