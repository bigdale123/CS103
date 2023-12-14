#######################################################
#  Name: Dylan Calvin
#  BlazerID: dylcal13
#  Assignment: HW2
#######################################################

def myName ():
    return "Dylan Calvin"

def myBlazerID():
    return "dylcal13"

def p(x):
    #print(x)           # Used for Debugging
    #print(type(x))     # Used for Debugging
    x = float(x)
    if x > 1 or x < 0:
        return 0
    else:
        return 1

def isOdd (n1):
    # print(type(n1))     #Used for debugging
    if type(n1) == int:
        if n1%2 != 0:
            return True
        else:
            return False
    else:
        return False

def grader (avg_exams, avg_hw, attendance):
    if attendance < 20:
        return False
    elif (avg_exams >= 70 and avg_hw >= 70) and (avg_exams >= 85 or avg_hw >= 85):
        return True
    else:
        return False

def tupleCounter(t):
    num_odd = 0
    for i in t:
        if isOdd(i) == True:
            num_odd += 1
    return num_odd

def cubeOfOdd(n2):
    i=1
    while i >= 1 and i < n2:
        if isOdd(i) == True:
            print("     " + str(i**3))
        i += 1

def sec2Days(n3):
    # initialize
    day = 0
    hour = 0
    minute = 0
    #process
    day = int(n3/86400)
    n3 = n3-(day*86400)
    hour = int(n3/3600)
    n3 = n3-(hour*3600)
    minute = int(n3/60)
    n3 = n3-(minute*60)
    #return
    return (str(day)+":"+str(hour)+":"+str(minute)+":"+str(int(n3)))

def cellPhoneBill(m,tx):
    if m <= 50 and tx <= 50:
        amount_before_tax = 15
    elif m <= 50 and tx > 50:
        amount_before_tax = 15+((tx-50)*0.15)
    elif m > 50 and tx <= 50:
        amount_before_tax = 15+((m-50)*0.25)
    else:
        amount_before_tax = 15+((m-50)*0.25)+((tx-50)*0.15)
    final_amount = (amount_before_tax + 0.44)
    return (final_amount + final_amount*0.05) #calculate tax w/ included .44 charge


##################
# Function Calls #
##################
print("My name is " + myName() + " and my BlazerID is " + myBlazerID())
print()
print("***************************************************")
print("The result of both test cases for p(x) are:")
print(" p(1)  = " + str(p(1)))
print(" p(2)  = " + str(p(2)))
print(" p(-1) = " + str(p(-1)))
print()
print("***************************************************")
print("The result of both test cases for isOdd are:")
print(" isOdd(5)   = " + str(isOdd(5)))
print(" isOdd(5.1) = " + str(isOdd(5.1)))
print()
print("***************************************************")
print("The result of all test cases for grader are:")
print(" grader(72,88,22)  = " + str(grader(72,88,22)))
print(" grader(66,100,24) = " + str(grader(66,100,24)))
print(" grader(100,90,18) = " + str(grader(100,90,18)))
print()
print("***************************************************")
print("The result of all test cases for tupleCounter are:")
print(" tupleCounter(2,4,6,7,9,121,1) = " + str(tupleCounter((2,4,6,7,9,121,1))))
print(" tupleCounter(1,3)             = " + str(tupleCounter((1,3))))
print(" tupleCounter(10,30,44)        = " + str(tupleCounter((10,30,44))))
print("***************************************************")
print("The result of all test cases for cubeOfOdd are:")
print(" cubeOfOdd(5) = ")
cubeOfOdd(5)
print(" cubeOfOdd(3) = ")
cubeOfOdd(3)
print(" cubeOfOdd(8) = ")
cubeOfOdd(8)
print("***************************************************")
print("The result of all test cases for sec2Days are:")
print(" sec2Days(750000) = " + sec2Days(750000))
print(" sec2Days(1234)   = " + sec2Days(1234))
print(" sec2Days(200000) = " + sec2Days(200000))
print("***************************************************")
print("The result of all test cases for cellPhoneBill are:")
print("cellPhoneBill(70,120) = " + str(cellPhoneBill(70,120)))
print("cellPhoneBill(50,50)  = " + str(cellPhoneBill(50,50)))
print("cellPhoneBill(127,30) = " + str(cellPhoneBill(127,30)))