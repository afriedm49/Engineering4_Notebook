import board
import digitalio
import time
led = digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
counter = 0
while counter < 5: # Blinks 5 times fast
    led.value = True
    time.sleep(.25)
    led.value = False
    time.sleep(.25)
    counter += 1

while True: # Blinks indefinitely
    led.value = True
    time.sleep(.8)
    led.value = False
    time.sleep(.8)
    