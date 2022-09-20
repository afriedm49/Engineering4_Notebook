# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LaunchPad1](#LaunchPad1)
* [LaunchPad2](#LaunchPad2)
* [LaunchPad3](#LaunchPad3)
* [LaunchPad4](#LaunchPad4)
* [CrashAvoidance1](#CrashAvoidance1)
* [CrashAvoidance2](#CrashAvoidance2)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## LaunchPad1

### Assignment Description

This assignment was to code the serial monitor to count down from 10 to 0, with one second in between. It prints "Liftoff!" after landing.

### Evidence 

![Video](images/Astronaut_pt1.mp4) 

### Wiring

N.A.

### Code
[Part 1 code](https://github.com/afriedm49/Engineering4_Notebook/blob/main/raspberry-pi/Astronaut1.py)

### Reflection

It was challenging at first to figure out the for loop, but easy once I got it. It important to make sure that your step is negative if you are trying to count down, or else you will need to do print(10-x) for each value of x from 0 to 10.
&nbsp;

## LaunchPad2

### Assignment Description

This assignment was to add on to part 1 by plugging in an external red LED which blinks as time goes down, and a green LED which stays on during liftoff.

### Evidence 

![Video](images/Astronaut2.mp4) 

### Wiring

![Pic](images/Astronaut2.png) 

### Code
[Part 2 code](https://github.com/afriedm49/Engineering4_Notebook/blob/main/raspberry-pi/Astronaut2.py)

### Reflection

Make sure you are using OUTPUT on your LED direction, and get your led to turn on and off within the for loop, so it continually repeats.

&nbsp;

## LaunchPad3

### Assignment Description

This assignment was to add on to parts 1 and 2 by connecting a button that starts the program.

### Evidence 

![Video](images/Astronaut3.mp4) 

### Wiring

<img src="images/Astronaut3.jpg" width="300" height="400" /> 

### Code
[Part 3 code](https://github.com/afriedm49/Engineering4_Notebook/blob/main/raspberry-pi/Astronaut3.py)

### Reflection

The tricky part on this assignment was making sure that the wiring was set up correct. It was much simpler than I originally thought, because the button only needed to be plugged in to 3V and an input PIN. Pressing the button closes the circuit, signalling a True button.value.

&nbsp;

## LaunchPad4

### Assignment Description

This assignment was to add on to parts 1, 2, and 3 by connecting a servo that spins before liftoff. It starts spinning at 3 seconds remaining, by 60 degrees, and 60 degrees more for seconds 2 and 1, until it's turned all the way 180 degrees.
### Evidence 

![Video](images/Astronaut4.mp4) 

### Wiring

<img src="images/Astronaut4.jpg" width="300" height="400" /> 

### Code
[Part 4 code](https://github.com/afriedm49/Engineering4_Notebook/blob/main/raspberry-pi/Astronaut4.py)

### Reflection

#### In order to create a "sweeping" effect, it is important to set a counter before the program begins:
```python
counter = 0
```

#### Each second within the for loop, the counter adds one, and sweep begins after 7 seconds:
```python
counter += 1 
if counter > 7: 
    servo1.angle += 60 
```
&nbsp;

## CrashAvoidance1

### Assignment Description

This assignment is to set up the wiring and simple programming of an accelerometer, the mpu6050.

### Evidence 

![Video](images/CrashAvoidance1.mp4) 

### Wiring

<img src="images/Crashavoidance1.jpg" width="300" height="400" /> 

### Code
[Crash Avoidance Code Part 1](https://github.com/afriedm49/Engineering4_Notebook/blob/main/raspberry-pi/CrashAvoidance1.py)

### Reflection

The wiring was the trickier part of this assignment. Make sure that the scl pin is connected to an scl applicable pin on the pico, and same with the sda pin. Also, make sure that you have a while loop printing the acceleration, and a time.sleep in place so the values don't run forever. 

As the output is a tuple, you are able to print only the x acceleration, for example, by typing print(mpu.acceleration[0]). Use [1] for y values and [2] for z values.

## CrashAvoidance2

### Assignment Description

This assignment is to make an LED turn on when the accelerometer is sideways.

### Evidence 

![Video](images/CrashAvoidance2.MOV) 

### Wiring

<img src="images/CrashAvoidance2.jpg" width="300" height="400" /> 

### Code
[Crash Avoidance Code Part 2](https://github.com/afriedm49/Engineering4_Notebook/blob/main/raspberry-pi/CrashAvoidance2.py)

### Reflection

Remember, because the output is a tuple, you are able to print only the x acceleration, for example, by typing print(mpu.acceleration[0]). Use [1] for y values and [2] for z values.
In order to complete this assignment, simply make the led turn on when mpu.acceleration[2] is equal to 0. Because it is hard to line it up exactly sideways, use a margin of error such as one shown below:

```python
while True:
    print(mpu.acceleration)
    if (-1 < mpu.acceleration[2] < 1):
        led.value = True
    else:
        led.value = False
```
&nbsp;

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
  [Test](raspberry-pi/test.py)      

### Test Image
  ![Test](images/raspberry.jfif) 
### Test GIF
  ![Test](images/Gatsbymeme.gif) 
