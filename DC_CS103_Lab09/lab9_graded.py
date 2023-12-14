import random
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

def winChecker(board):
    """
    winChecker(board): given a 2-d array, of length 3x3, the function determines if
        the game should be over yet.

    Parameters:
        board (list of lists): the board passed from ticTacToe() to this function

    Returns a one or nothing
    """
    #HR1-user
    if board[0] == [1,1,1]:
        print("You Won!")
        return 1
    #HR2-user
    elif board[1] == [1,1,1]:
        print("You Won!")
        return 1
    #HR3-user
    elif board[2] == [1,1,1]:
        print("You Won!")
        return 1
    #VC1-user
    elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        print("You Won!")
        return 1
    #VC2-user
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        print("You Won!")
        return 1
    #VC3-user
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        print("You Won!")
        return 1
    #D1-user
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        print("You Won!")
        return 1
    #D2-user
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        print("You Won!")
        return 1
    #HR1-comp
    if board[0] == [2,2,2]:
        print("You Lost.")
        return 1
    #HR2-comp
    elif board[1] == [2,2,2]:
        print("You Lost.")
        return 1
    #HR3-comp
    elif board[2] == [2,2,2]:
        print("You Lost.")
        return 1
    #VC1-comp
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        print("You Lost.")
        return 1
    #VC2-comp
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        print("You Lost.")
        return 1
    #VC3-comp
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        print("You Lost.")
        return 1
    #D1-comp
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        print("You Lost.")
        return 1
    #D2-comp
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        print("You Lost.")
        return 1
    elif (0 not in board[0] and 0 not in board[1] and 0 not in board[2]) == True:
        print("Stalemate!")
        return 1

def ticTacToe():
    """
    ticTacToe(): When called, initiates a game of tic tac toe against "AI" (random choices).

    No parameters

    Nothing being returned
    """
    board = [[0,0,0],[0,0,0],[0,0,0]]
    is_won = 0
    who_won = 0
    user_row = 0
    user_column = 0
    computer_row = 0
    computer_column = 0
    plays = []
    print(board[0])
    print(board[1])
    print(board[2])
    while is_won != 1:
        user_row = int(input("Please enter row choice: "))-1
        user_column = int(input("Please enter column choice: "))-1
        if (user_row <= 2) and (user_column <= 2):
            if (str(user_row)+","+str(user_column)) not in plays:
                    board[user_row][user_column] = 1
                    plays.append(str(user_row)+","+str(user_column))
                    print(plays)
                    computer_row = random.randint(0,2)
                    computer_column = random.randint(0,2)
                    while (str(computer_row)+","+str(computer_column)) in plays:
                        if len(plays) == 9:
                            break
                        else:
                            computer_row = random.randint(0,2)
                            computer_column = random.randint(0,2)
                    print(str(computer_row)+","+str(computer_column))
                    board[computer_row][computer_column] = 2
                    plays.append(str(computer_row)+","+str(computer_column))


                    is_won = winChecker(board)
                    print(board[0])
                    print(board[1])
                    print(board[2])

            else:
                print(" That spot has already been played, pick another spot.")
        else:
            print("Your row or column was too big, try again.")

def houseTree():
    """
    houseTree(): When called, draws a house and a tree in turtle

    No parameters

    Nothing returned
    """
    wn = Screen()
    up()
    goto(-150,0)
    down()
    pencolor("black")
    begin_fill()
    fillcolor("tan")
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    end_fill()
    up()
    setheading(0)
    left(90)
    forward(100)
    down()
    begin_fill()
    fillcolor("brown")
    right(45)
    forward(70.71)
    right(90)
    forward(70.71)
    end_fill()
    up()
    goto(0,0)
    setheading(0)
    goto(-115,0)
    down()
    begin_fill()
    fillcolor("brown")
    left(90)
    forward(50)
    right(90)
    forward(30)
    right(90)
    forward(50)
    right(90)
    forward(30)
    end_fill()
    up()
    setheading(90)
    forward(50)
    left(90)
    forward(10)
    down()
    begin_fill()
    fillcolor("light blue")
    forward(15)
    left(90)
    forward(15)
    left(90)
    forward(15)
    left(90)
    forward(15)
    end_fill()
    right(90)
    up()
    forward(50)
    down()
    begin_fill()
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    end_fill()
    up()
    goto(100,0)
    setheading(0)
    begin_fill()
    fillcolor("brown")
    forward(30)
    left(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(40)
    end_fill()
    up()
    left(180)
    forward(40)
    down()
    setheading(180)
    begin_fill()
    fillcolor("green")
    forward(50)
    right(110)
    forward(200)
    right(140)
    forward(200)
    setheading(180)
    forward(50)
    end_fill()
    done()

print("My Name is =",myName(), " and my BlazerID is =",myBlazerID())
ticTacToe()
houseTree()
