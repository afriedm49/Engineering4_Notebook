
import board
import digitalio
import time
blinkled = digitalio.DigitalInOut(board.GP19)
blinkled.direction=digitalio.Direction.OUTPUT
staticled = digitalio.DigitalInOut(board.GP15)
staticled.direction=digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.pull = digitalio.Pull.DOWN
while True:
  if button.value == True:
    for i in range(10, 0, -1):
        print(i)
        blinkled.value = True
        time.sleep(.5)
        blinkled.value = False
        time.sleep(.5)
    print("Liftoff!")
    while True:
      staticled.value = True