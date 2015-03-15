#!/usr/bin/env python
from MCP3008 import *
from Setup import *
import RPi.GPIO as GPIO

DEBUG = 0

# IR proximity sensor connected to adc #0
sensor_adc = 0

#--------------------------------------------------

weAre= "Liam,Jack,Andrew,Ty, and Samantha?"
sound = "Group\ 1a.wav"
print "what's goin on my homedogs- " +weAre
while True:
        # read the analog pin
	proximity = readadc(sensor_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
	print proximity
	if proximity > 400:
		if sound == "Group\ 1a.wav":
			os.system("aplay " + sound)
			sound = "Group\ 1b.wav"
		elif sound == "Group\ 1b.wav":
			os.system("aplay " + sound)
			sound = "Group\ 1c.wav"
		elif sound == "Group\ 1c.wav":
			os.system("aplay " + sound)
			sound = "Group\ 1e.wav"
		elif sound == "Group\ 1e.wav":
			os.system("aplay " + sound)
			sound = "Group\ 1a.wav"
        # sleep for half a second
	time.sleep(0.5)