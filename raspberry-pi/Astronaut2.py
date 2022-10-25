import board
import digitalio
import time
blinkled = digitalio.DigitalInOut(board.GP1)        #blink LED is the red led that blinks
blinkled.direction=digitalio.Direction.OUTPUT
staticled = digitalio.DigitalInOut(board.GP8)       #static LED is the green led that stays on 
staticled.direction=digitalio.Direction.OUTPUT
for i in range(10, 0, -1):
    print(i)
    blinkled.value = True
    time.sleep(.5)
    blinkled.value = False
    time.sleep(.5)
print("Liftoff!")
while True:
  staticled.value = True
