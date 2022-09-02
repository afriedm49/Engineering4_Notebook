import board
import digitalio
import time
led = digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT
for i in range(10, 0, -1):
    print(i)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)
print("Liftoff!")
led.value = True