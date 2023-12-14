from turtle import *

def myName():
    """
    myName(): upon calling, the function returns my name.

    No parameters needed.

    Example: print(myName())
    Output:
        Dylan Calvin
    """
    return "Dylan Calvin"
def myBlazerID():
    """
    myBlazerID(): upon calling, the function returns my BlazerID.

    No parameters needed.

    Example: print(myBlazerID())
    Output:
        dylcal13
    """
    return "dylcal13"

def tSquare(n1):
    """
    tSquare(n1): given a length, n1, the function draws a square whose side lengths
        are n1 on a pred-defined turtle screen (if screen hasn't been made, won't work)

    Parameters:
        n1 (int): the given side length given to the function

    Returns a square on the turtle screen
    """
    for i in range(0,4):
        forward(n1)
        right(90)

def tCircle(n2):
    """
    tCircle(n2): given an integer, n2, the function uses a pre-defined function
        to draw a red circle of radius r on a pre-defined turtle screen.

    Parameters:
        n2 (int): The radius of the circle as an integer, given to the function.

    Return a red circle on the turtle screen.
    """
    pencolor("red")
    circle(n2)

def tTriangle(n3):
    """
    tTriangle(n3): Given a integer, n3, the function draws a equilateral triangle on
        a pre-defined turtle screen
        - The triangle is solid yellow with blue sides.

    Parameters:
        n3 (int): The integer that is the length of all sides given to the function

    Returns picture of triangle in turtle screen
    """
    pencolor("blue")
    setheading(0)
    begin_fill()
    fillcolor("yellow")
    forward(n3)
    left(120)
    forward(n3)
    left(120)
    forward(n3)
    end_fill()

wn = Screen()

print("My Name is =",myName(), " and my BlazerID is =",myBlazerID())
tSquare(50)
tCircle(25)
tTriangle(100)

done()
