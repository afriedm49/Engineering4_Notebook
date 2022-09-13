
import board
import digitalio
import pwmio
from adafruit_motor import servo
import time
blinkled = digitalio.DigitalInOut(board.GP19)
blinkled.direction=digitalio.Direction.OUTPUT
staticled = digitalio.DigitalInOut(board.GP15)
staticled.direction=digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.pull = digitalio.Pull.DOWN
pwm_servo = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0
counter = 0
while True:
  if button.value == True:
    for i in range(10, 0, -1):
        print(i)
        blinkled.value = True
        time.sleep(.5)
        blinkled.value = False
        time.sleep(.5)
        counter += 1
        if counter > 7:
            servo1.angle += 60
    print("Liftoff!")
    while True:
      staticled.value = True