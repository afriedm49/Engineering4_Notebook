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
    '(':'-.--.', ')':'-.--.-', ' ': '/'}        #' ' was added to the dictionary, so a slash would appear between each word in the morse message.

modifier = 0.25             # variables show the amount of time for each to rest before blinking again.
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
        if item == '.':         #blinks an LED for the "dot_time", which is done for each type of letter below
            led.value = True
            time.sleep(dot_time)
            led.value = False
        elif item == '-':
            led.value = True
            time.sleep(dash_time)
            led.value = False
        
        if item == ' ':                     #Message blinks between letters
            time.sleep(between_letters)
        elif item == '/':                   #blinks for a different time between each word
            time.sleep(between_words)
        else:
            time.sleep(tap_delay)
