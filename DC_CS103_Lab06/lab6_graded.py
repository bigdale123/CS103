import random
########################################
#  Name: Dylan Calvin
#  BlazerID: dylcal13
#  Assignment: Lab 6 (graded)
########################################


def iCube(n):
    """
    iCube(n): given an integer, n, the function will print the cube of every integer less than n.

    Parameters:
        n (int): the integer used to define the upper limit, and is passed into the function when called.

    Example: iCube(5)
    Output:
        1
        8
        27
        64
    """
    #Error Trapping
    if type(n) != int:
        print("ERROR in iCube(): recieved a non-int value for input.")
        return
    if n < 0:
        print("ERROR in iCube(): recieved a negative value for input, input must be a positive integer.")
    #Function
    i = 0
    while i < n:
        print(i**3)
        i += 1

def sConcatenate():
    """
    sConcatenate(): the function asks the user to input a string, over and over until the user enters the string
        "done". upon entering done, the function adds every string that was input (except for "done") together
        into one string, each input being delimited with spaces.

    Example: sConcatenate()
    Output:
        Enter a string: hello
        Enter a string: world
        Enter a string: done
         Your concatenated string is: hello world
    """
    choice = ""
    list_to_concat = []
    ret_string = ""
    while choice != "done":
        choice = input("Enter a string: ")
        if choice != "done": list_to_concat.append(choice+" ")
    for i in list_to_concat:
        ret_string += i
    print("Your concatenated string is: "+ret_string)

def guessNumber():
    """
    guessNumber(): The function will sstart by guessing a random integer, num_to_guess. The user then gets asked to
        Guess what that number is, and then the user is told if they either guessed right, guessed too high, or
        guessed too low. upon guessing the number correctly, the function tells the user what the number was
        and how many tries it took

    Example: guessNumber()
    Output:
        Guess a number between 1 and 100: 25
         You guessed too high!
        Guess a number between 1 and 100: 15
         You guessed too low!
        Guess a number between 1 and 100: 10
        ------------------------------------
        You guessed the correct number! it was 10
        you guessed the number in 2 tries
    """
    choice = ""
    i = 0
    num_to_guess = random.randint(1,100)
    while choice != num_to_guess:
        choice = int(input("Guess a number between 1 and 100: "))
        if choice == num_to_guess:
            print("----------------------------------------------")
            print("You guessed the correct number! it was "+str(choice))
            print("You guessed the number in "+str(i)+" tries.")
            break
        elif choice > num_to_guess:
            print(" You guessed too High!")
        elif choice < num_to_guess:
            print(" You guessed too low!")
        i += 1

print("****** Results of iCube() ******")
print("Result 1: iCube(5)")
iCube(5)
print("Result 2: iCube(7)")
iCube(7)
print("Result 3: iCube(9)")
iCube(9)
print()
print("****** Results of sConcatenate() ******")
sConcatenate()
print()
print("****** Results of guessNumber() ******")
guessNumber()



