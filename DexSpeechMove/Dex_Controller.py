from gopigo import *
import atexit
from time import sleep
import time

atexit.register(stop())

def Dir(Direction):
	Wait_speed = 1
	print("Moving ") + Direction
	forwards_list = ['FORWARDS','FORD','UP']
	if any(Direction.upper() in s for s in forwards_list):
		fwd()
		sleep(Wait_speed)
		stop()
	elif Direction.upper() == "BACK":
		bwd()
		sleep(Wait_speed)
		stop()
	elif Direction.upper() == "LEFT":
		left()
		sleep(Wait_speed)
		stop()
	elif Direction.upper() == "RIGHT":
		right()
		sleep(Wait_speed)
		stop()
	else:
		stop()