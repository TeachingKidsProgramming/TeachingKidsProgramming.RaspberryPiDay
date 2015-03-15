#!/usr/bin/env python
from MCP3008 import *
from Setup import *
import RPi.GPIO as GPIO

DEBUG = 0

# IR proximity sensor connected to adc #0
sensor_adc = 0


play_sound1 = 'aplay alarm_beep.wav'
play_sound2 = 'aplay alarm_beepwef.wav'
last_sound = 1

while True:
        # read the analog pin
        proximity = readadc(sensor_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)

        if DEBUG:
                print "proximity:", proximity

	if proximity >= 400:
		if last_sound == 1:
			os.system(play_sound1)
			last_sound = 0
		else:
			os.system(play_sound2)
			last_sound = 1

        # sleep for half a second
        time.sleep(0.5)