import board
import math
def triArea(x1, y1, x2, y2, x3, y3):    #creates a triArea function, taking inputs of 3 x values and 3 y values
    x1 = float(x1)                      #the inputs need to be converted to floats to do math 
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    area = abs(x1 * (y2-y3) + x2 * (y3-y1) + x3 *(y3-y2))       #area formula
    return area
while True:

    try:    #try is used because if an error occurs, it will print the error message, and then restart, instead of stopping the code
        [xcoor1, ycoor1] = input("Enter coordinate 1: ").split(",")                 #takes an input of 2 variables using the split method
        [xcoor2, ycoor2] = input("Enter coordinate 2: ").split(",")
        [xcoor3, ycoor3] = input("Enter coordinate 2: ").split(",")
        print("The area of the triangle with points (" + xcoor1 + ", " + ycoor1 + ")," + " (" + xcoor2 + ", " + ycoor2 + ")," + " (" + xcoor3 + ", " + ycoor3 + ") is " + str(triArea(xcoor1, ycoor1, xcoor2, ycoor2, xcoor3, ycoor3)))
    # this prints area calling the triArea function
    except:
        print("Error")
