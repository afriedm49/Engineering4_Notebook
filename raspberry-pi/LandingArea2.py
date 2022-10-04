import board
import math
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import digitalio
import busio
import displayio
import terminalio
import time
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

sda_pin = board.GP12
scl_pin = board.GP13
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def triArea(x1, y1, x2, y2, x3, y3):
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    area = abs(x1 * (y2-y3) + x2 * (y3-y1) + x3 *(y3-y2))
    return area
    
while True:
    splash = displayio.Group()
    vline = Line(64,0,64,64, color=0xFFFF00)
    splash.append(vline)
    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)

    centerpoint = Circle(64, 32, 3, outline=0xFFFF00)
    splash.append(centerpoint)

    try:
        [xcoor1, ycoor1] = input("Enter coordinate 1: ").split(",")
        [xcoor2, ycoor2] = input("Enter coordinate 2: ").split(",")
        [xcoor3, ycoor3] = input("Enter coordinate 3: ").split(",")
        print("The area of the triangle with points (" + xcoor1 + ", " + ycoor1 + ")," + " (" + xcoor2 + ", " + ycoor2 + ")," + " (" + xcoor3 + ", " + ycoor3 + ") is " + str(triArea(xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3)))
        xcoor1 = int(xcoor1) + 64
        xcoor2 = int(xcoor2) + 64
        xcoor3 = int(xcoor3) + 64
        ycoor1 = -int(ycoor1) + 32
        ycoor2 = -int(ycoor2) + 32
        ycoor3 = -int(ycoor3) + 32

    except:
        print("Error")

    triangle = Triangle(xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3, outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)