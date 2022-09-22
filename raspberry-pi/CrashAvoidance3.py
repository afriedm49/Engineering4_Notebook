from adafruit_display_text import label
import adafruit_displayio_ssd1306
import board
import digitalio
import busio
import adafruit_mpu6050
import displayio
import terminalio
import time
led = digitalio.DigitalInOut(board.GP2)
led.direction=digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)

display.show(splash)
