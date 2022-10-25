import board
import math
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import digitalio
import busio
import displayio
import terminalio
import time
from adafruit_display_shapes.line import Line


displayio.release_displays()

sda_pin = board.GP12
scl_pin = board.GP13
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP16)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
# A dictionary is intialized above, containing definitions of each letter as dashes and dots in morse.
    
while True:
    morseMessage = "" # starts an empty string to be added to 
    splash = displayio.Group()
    message = str(input("Enter your message to be converted to Morse Code: ")).upper()  # message is taken as input
    if message == "-Q": #quits if -q is typed
        break
    for letter in message:      
        morseMessage += MORSE_CODE[letter]      #adds each morse letter to the morse message
        morseMessage += '/'                     #puts a slash between each letter
    print(morseMessage)
