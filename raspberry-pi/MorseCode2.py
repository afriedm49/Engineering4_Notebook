import board
import math
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT

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
    '(':'-.--.', ')':'-.--.-', ' ': '/'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
tap_delay = modifier
between_letters = 3*modifier
between_words = 4 * modifier

    
while True:
    morseMessage = ""
    message = str(input("Enter your message to be converted to Morse Code: ")).upper()
    if message == "-Q":
        break
    for letter in message:
        morseMessage += MORSE_CODE[letter]
        if letter != ' ':
            morseMessage += ' '
    print(morseMessage)
    for item in morseMessage:
        if item == '.':
            led.value = True
            time.sleep(dot_time)
            led.value = False
        elif item == '-':
            led.value = True
            time.sleep(dash_time)
            led.value = False
        
        if item == ' ':
            time.sleep(between_letters)
        elif item == '/':
            time.sleep(between_words)
        else:
            time.sleep(tap_delay)