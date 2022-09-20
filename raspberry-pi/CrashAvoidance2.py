import board
import digitalio
import busio
import adafruit_mpu6050
import time
led = digitalio.DigitalInOut(board.GP2)
led.direction=digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
while True:
    print(mpu.acceleration)
    if (-1 < mpu.acceleration[2] < 1):
        led.value = True
    else:
        led.value = False