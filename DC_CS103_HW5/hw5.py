from turtle import *
import random
#Mandatory functions
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

#HW Functions
def longest(L):
    """
    longest(L): given a nonempty list of strings, finds the longest even-length string that ends with the suffix -ing.

    Parameters:
        L (list): List containing strings that is passed into the function

    Returns:
        longest (string): The longest even length string found by the function that ends in -ing. (Will return empty string if nothing meets requirements.)
    """
    longest = ""
    for i in L:
        if len(i) > 3:
            #print(i)
            if i[-3:] == "ing":
                #print(i[-3:])
                if (len(i) % 2) == 0:
                    #print(i)
                    if len(i) > len(longest):
                        longest = i
    return longest

def arglongest(L):
    """
    argLongest(L): given a nonempty list of strings, finds the longest even-length string that ends with the suffix -ing. Almost identical to longest(),
        except this function returns the index of the longest even length word ending in -ing.

    Parameters:
        L (list): List containing strings that is passed into the function

    Returns:
        longest_index (int): The index of longest even length string found by the function that ends in -ing. (Will return empty string if nothing meets requirements.)
    """
    longest = 0
    longest_index = -1
    for i in range(len(L)):
        if len(L[i]) > 3:
            #print(i)
            if L[i][-3:] == "ing":
                #print(i[-3:])
                if (len(L[i]) % 2) == 0:
                    #print(i)
                    if len(L[i]) > longest:
                        longest_index = i
                        longest = len(L[i])
    return longest_index

def flagInitials():
    """
    flagInitials(): Upon calling, writes my name in maritime letter flags using turtle graphics.

    No Parameters, nothing returned. Will display a picture, though.
    """
    #  This bit right here just speeds the turtle up.
    speed("fastest")

    
    w=Screen()
    up()
    goto(random.randint(-200,0),random.randint(-200,0))
    down()
    w = random.randint(100,200)
    gap = random.randint(1,10)
    setheading(0)

    #-----------
    # Flag "D"
    #-----------

    #Black Border
    pencolor("black")
    begin_fill()
    fillcolor("yellow")
    for i in range(4):
        forward(w)
        left(90)
    setheading(0)
    end_fill()
    #Fill in blue in middle
    up()
    goto(xcor(),ycor()+(w/5))
    down()
    begin_fill()
    fillcolor("blue")
    left(90)
    forward(w*(3/5))
    right(90)
    forward(w)
    right(90)
    forward(w*(3/5))
    right(90)
    forward(w)
    end_fill()

    #Prepare for next letter
    up()
    left(90)
    forward(w/5)
    setheading(0)
    forward(w+gap)
    down()

    #-----------
    # Flag "T"
    #-----------

    #Create border
    for i in range(4):
        forward(w)
        left(90)

    #Red Third
    begin_fill()
    fillcolor("red")
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    end_fill()
    up()

    #White Third (Skip the physical space)
    forward(w*(2/3))
    down()
    #Blue Third
    begin_fill()
    fillcolor("blue")
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    end_fill()
    up()

    #Setup for final cube
    forward((w/3)+gap)
    down()

    #-----------
    # Flag "C"
    #-----------

    #Create border
    for i in range(4):
        forward(w)
        left(90)
    #Create Blue fifth 1
    begin_fill()
    fillcolor("blue")
    left(90)
    forward(w/5)
    right(90)
    forward(w)
    right(90)
    forward(w/5)
    right(90)
    forward(w)
    end_fill()
    up()
    right(90)

    #Create White fifth 1 (skip region)
    forward(w*(2/5))
    #Create Red fifth
    right(90)
    down()
    begin_fill()
    fillcolor("red")
    left(90)
    forward(w/5)
    right(90)
    forward(w)
    right(90)
    forward(w/5)
    right(90)
    forward(w)
    end_fill()
    up()
    right(90)
    #Create White Fifth 2 (skip region)
    forward(w*(2/5))
    #Create Blue Fifth 2
    right(90)
    down()
    begin_fill()
    fillcolor("blue")
    left(90)
    forward(w/5)
    right(90)
    forward(w)
    right(90)
    forward(w/5)
    right(90)
    forward(w)
    end_fill()
    up()
    right(90)
    #done
    done()







# Function Calls
print("My Name is =", myName(), "and my BlazerId is =",myBlazerID())
print(longest(["aing", "bb", "ccing","ddding", "zzzzzzzzzzzz"]))
print(longest(["swimming", "flying", "coding", "abracadabra UAB CS103","yoo", "python programming"]))
print(longest(["robinhood" ,"amazon", "ding", "bing"]))
print(longest(["fishing", "doesn’t", "count", "it", "is", "not even-length"]))
print("--")
print(arglongest(["aing", "bb", "ccing","ddding", "zzzzzzzzzzzz"]))
print(arglongest(["swimming", "flying", "coding", "abracadabra UAB CS103","yoo", "python programming"]))
print(arglongest(["robinhood" ,"amazon", "ding", "bing"]))
print(arglongest(["fishing", "doesn’t", "count", "it", "is", "not even-length"]))
print(arglongest(["aing","bbing","bruh","cccing"]))
flagInitials()
