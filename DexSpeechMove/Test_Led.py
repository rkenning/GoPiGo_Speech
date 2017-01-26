import Led_Control as led

if __name__ == '__main__':     # Program start from here
	led.setup()
	
	try:
		led.LED_Dir("FORWARDS")
		led.LED_Dir("BACK")
		led.LED_Dir("LEFT")
		led.LED_Dir("RIGHT")

	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		led.destroy()

led.destroy()   