#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
import time



LedPin1 = 32    # Left (Battry at bottom)
LedPin2 = 36    # Bottom
LedPin3 = 38    # Right
LedPin4 = 40    # Top

pins = [LedPin1,LedPin2,LedPin3,LedPin4]

sleep_time = .04


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	for item in pins:
		GPIO.setup(item, GPIO.OUT,initial=GPIO.LOW)
	

def spinning():
	for _ in range(4):
		for item in pins:
			GPIO.output(item, GPIO.HIGH)     # led off
			sleep(sleep_time)
			GPIO.output(item, GPIO.LOW)     # led off
			sleep(sleep_time)

def flash():
	flash_sleep  =.2
	# Loop 4 times
	for _ in range(2):
		# led on
		GPIO.output(pins[0], GPIO.HIGH)
		GPIO.output(pins[1], GPIO.HIGH)
		GPIO.output(pins[2], GPIO.HIGH)
		GPIO.output(pins[3], GPIO.HIGH)
		sleep(flash_sleep)

		GPIO.output(pins[0], GPIO.LOW)
		GPIO.output(pins[1], GPIO.LOW)
		GPIO.output(pins[2], GPIO.LOW)
		GPIO.output(pins[3], GPIO.LOW)
		
		sleep(flash_sleep)


def LED_Dir(Direction):
	speed2 = .5
	forwards_list = ['FORWARDS','FORD','UP']

	if any(Direction.upper() in s for s in forwards_list):
		GPIO.output(pins[1], GPIO.HIGH)     # led off
		sleep(speed2)
		GPIO.output(pins[1], GPIO.LOW)     # led off
		sleep(speed2)
	elif Direction.upper() == "BACK":
		GPIO.output(pins[3], GPIO.HIGH)     # led off
		sleep(speed2)
		GPIO.output(pins[3], GPIO.LOW)     # led off
	elif Direction.upper() == "LEFT":
		GPIO.output(pins[2], GPIO.HIGH)     # led off
		sleep(speed2)
		GPIO.output(pins[2], GPIO.LOW)     # led off
		sleep(speed2)
	elif Direction.upper() == "RIGHT":
		GPIO.output(pins[0], GPIO.HIGH)     # led off
		sleep(speed2)
		GPIO.output(pins[0], GPIO.LOW)     # led off
		sleep(speed2)
	else:
		flash() #Flash all lights as there is an error


def destroy():
	for item in pins:
		GPIO.output(item, GPIO.HIGH)     # led off
	
	GPIO.cleanup()                     # Release resource


