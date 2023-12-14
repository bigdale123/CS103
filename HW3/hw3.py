###############################################
# Name: Dylan Calvin
# BlazerID: dylcal13
# Assignment: Homework 3
###############################################
import math

def myName():
    return "Dylan Calvin"
def myBlazerID():
    return "dylcal13"

def listBuilder(l1, length):
    """
    listBuilder(l1, length) : Given a list of strings and a length, listBuilder will check each list element
    to see if it's length matches the one specified and then return a list that contains all elements whose 
        length meets the specified requirement.

    Example: listBuilder(["hats","come","in","several","different","forms"],4)
      Output: ["hats","come"]
    """
    # Error Trapping
    for i in l1:
        if type(i) != str:
            print("ERROR in listBuilder(): list contains a non-string value.")
            return
    if type(length) != int:
        print("ERROR in listBuilder(): length specification is a non-integer value")
        return
    # Function
    ret_list = []
    for i in l1:
        if len(i) == length:
            ret_list.append(i)
    return ret_list

def isLetter(s):
    """
    isLetter(s) : given a string, s, isLetter removes all non-alphabetical characters from the string.

    Example: isLetter("CS103 is kind of fun.")
        Output: "CSiskindoffun"
    """
    # Error Trapping
    if type(s) != str:
        print("ERROR in isLetter(): recieved a non-string input.")
        return
    # Function
    replace_list = []
    for i in range(0,len(s)):
        if (s[i].isalpha() == False) and (s[i] in replace_list) == False:
            replace_list.append(s[i])
    for i in replace_list: # seperate from other for loop, replacing with "" changes length and breaks loop
        s = s.replace(i,"")
    return s

def elementLengthIsIndex(l2):
    """
    elementLengthIsIndex(l2): Takes a list of strings as input and return every element of the list whose
        length is equal to the index of it's position.

    Example: elementLengthIsIndex(["","cyan","gold","red","blue"])
        Output: ["","red","blue"]
    """
    if type(l2) != list:
        print("ERROR in elementLengthIsIndex(): recieved non-list value for input.")
    new_list = []
    for i in range(len(l2)):
        if len(l2[i]) == i:
            new_list.append(l2[i])
    return new_list

def typeMatters(par):
    """
    typeMatters(par): given an input, typeMatters will check what type the input is and perform specific
        actions on par.
      - If par is a string, it will return the string multiplied by its length.
        - Example: typeMatters("hello") = "hellohellohellohellohello"
      - If par is a integer, it will return every number from one to the integer.
        - Example: typeMatters(8) = "1 2 3 4 5 6 7 8"
      - If par is a float, will return the string "I am a float of value: " plus the value of the float
        - Example: typeMatters(5.634) = "I am a float of value: 5.634"
      - If par is a list, it will sort and reverse the list.
        - Example: typeMatters([23,8,4,16,15,42]) = [42,23,16,15,8,4]
      - If par does not match any of the previous types, it will return a statement stating that it does not match.
        - Example: typeMatters((3,4)) = "I am not a string, int, float, or list."
    """
    # no error trapping required
    if type(par) == str:
        return par*5
    elif type(par) == int:
        new_return = ""
        for i in range(1,par+1):
            new_return = new_return + str(i) + " " 
        return new_return
    elif type(par) == float:
        return "I am a float of value: "+str(par)
    elif type(par) == list:
        par.sort()
        par.reverse()
        return par
    else:
        return "I am not a string, int, float, or list."

def paintTheRoom(length, width, height):
    """
    paintTheRoom(length,width,height): given a length, width, and height of a room, paintTheRoom calculates
        how many whole gallons of paint are required to paint all 4 walls and the ceiling of the room.
      -Note : it is assumed that one gallon of paint covers 400 square feet.
    Example: paintTheRoom(10,12,8) = 2
    """
    #Error Trapping
    error_state = 0 #used to check each condition without needing return in each statement.
    if (type(length) != int) and (type(length) != float):
        print("ERROR in paintTheRoom(): recieved a non-numeric value for length input.")
        error_state = 1
    if (type(width) != int) and (type(width) != float):
        print("ERROR in paintTheRoom(): recieved a non-numeric value for width input.")
        error_state = 1
    if (type(height) != int) and (type(height) != float):
        print("ERROR in paintTheRoom(): recieved a non-numeric value for height input")
        error_state = 1
    #function
    if error_state == 1:
        return
    else:
        return math.ceil(((((2*length+2*width)*height)+(length*width))/400))            


# Calling Functions
print("My Name is =", myName(), " and my BlazerId is =",myBlazerID())
print()
print("****** Result(s) of listBuilder() ******")
print(" listBuilder([“Hello”, “I”, “am”, “a”, “list”],4) = ",str(listBuilder(["Hello", "I", "am", "a", "list"],4)))
print(" listBuilder([“Homework”, “is”, “fun”],8) = ",str(listBuilder(["Homework", "is", "fun"],8)))
print(" listBuilder([“CS103”, “is”, “the”, “best”],8) = ",str(listBuilder(["CS103", "is", "the", "best"],8)))
print()
print("****** Result(s) of isLetter() ******")
print(" isLetter(\"CS103 is kind of fun.\") = ",str(isLetter("CS103 is kind of fun.")))
print(" isLetter(\"Spaces  and  punctuation don’t count!\") = ",str(isLetter("Spaces  and  punctuation don’t count!")))
print(" isLetter(\"This is Hw3\") = ",str(isLetter("This is Hw3")))
print(" isLetter(1) = ",str(isLetter(1)))
print()
print("****** Result(s) of elementLengthIsIndex() ******")
print(" elementLengthIsIndex([\"I'm\",\"a\",\"tricky\",\"one\"]) = ",str(elementLengthIsIndex(["I'm","a","tricky","one"])))
print(" elementLengthIsIndex(['',  'cyan',  'gold',  'red', 'blue']) = ",str(elementLengthIsIndex(['',  'cyan',  'gold',  'red', 'blue'])))
print(" elementLengthIsIndex(['0', '1', '22', '333', '4']) = ",str(elementLengthIsIndex(['0', '1', '22', '333', '4'])))
print()
print("****** Result(s) of typeMatters() ******")
print(" typeMatters(\"hello\") = ",str(typeMatters("hello")))
print(" typeMatters(8) = ",str(typeMatters(8)))
print(" typeMatters(5.634) = ",str(typeMatters(5.634)))
print(" typeMatters([23, 8, 4, 16, 15, 42]) = ",str(typeMatters([23, 8, 4, 16, 15, 42])))
print(" typeMatters((3,4)) = ",str(typeMatters((3,4))))
print()
print("****** Result(s) of paintTheRoom() ******")
print(" paintTheRoom(10,12,8) = ",str(paintTheRoom(10,12,8)))
print(" paintTheRoom(75,85,50) = ",str(paintTheRoom(75,85,50)))
print(" paintTheRoom(1,1,1) = ",str(paintTheRoom(1,1,1)))