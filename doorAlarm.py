import time
import RPi.GPIO as io
io.setmode(io.BCM)

door_pin = 17

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

while True:
	if io.input(door_pin):
		print("Door Alarm!")
	time.sleep(1)