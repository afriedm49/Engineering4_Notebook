from adafruit_display_text import label
import adafruit_displayio_ssd1306
import board
import digitalio
import busio
import adafruit_mpu6050
import displayio
import terminalio
import time
displayio.release_displays()            #resets the display

led = digitalio.DigitalInOut(board.GP2)
led.direction=digitalio.Direction.OUTPUT
sda_pin = board.GP12       # Both the display and the accelerometer use the same sda and scl pins
scl_pin = board.GP13
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)       #sets address of mpu
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)         #sets address of display 
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
while True:
    splash = displayio.Group()
    title = "ANGULAR VELOCITY"
    xvelocity = "X-velocity: " + str(round(mpu.gyro[0], 3))     #gyro method prints velocity, and [0] signifies x, [1] signifies y, and [2] signifies z.
    yvelocity = "Y-velocity: " + str(round(mpu.gyro[1], 3))
    zvelocity = "Z-velocity: " + str(round(mpu.gyro[2], 3))
    text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)                                                             #This adds the text to the splash
    xlabel = label.Label(terminalio.FONT, text= xvelocity, color=0xFFFF00, x=5 , y=20)
    splash.append(xlabel)
    ylabel = label.Label(terminalio.FONT, text= yvelocity, color=0xFFFF00, x=5 , y=35)
    splash.append(ylabel)
    zlabel = label.Label(terminalio.FONT, text= zvelocity, color=0xFFFF00, x=5 , y=50)
    splash.append(zlabel)
    display.show(splash)                #finally shows the splash on the display
