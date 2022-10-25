import board  
import digitalio
import time
led = digitalio.DigitalInOut(board.LED)     # sets up LED in these 2 lines
led.direction=digitalio.Direction.OUTPUT    
for i in range(10, 0, -1):      # for loop to print numbers 10 through 0
    print(i)
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)
print("Liftoff!")
led.value = True        #leaves LED on after the loop ends
