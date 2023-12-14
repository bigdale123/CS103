#################################################
#  Name: Dylan Calvin
#  BlazerID: dylcal13
#  Assignment: Lab 5 (Graded)
#################################################

def stringSlicer(s1):
    # Error Trapping
    if type(s1) != str:
        print("ERROR in stringSlicer(): Recieved non-string value for input.")
        return
    # The actual function
    if len(s1) < 2:
        return ""
    else:
        return str(s1[:2]+s1[-2:])

def stringChanger(s1):
    # Error Trapping
    if type(s1) != str:
        print("ERROR in stringChanger: Recieved non-string value for input.")
        return

    #The actual function
    if len(s1) < 3:
        return s1
    else:
        if s1[-3:] == "ing":
            return s1+"ly"
        else:
            return s1+"ing"

def smallestSum(l1,l2):
    # Error Trapping
    if type(l1) != list and type(l2) != list:
        print("ERROR in smallestSum(): Recieved non-list value for both inputs.")
        return
    if type(l1) != list:
        print("ERROR in smallestSum(): Recieved non-list value for first input.")
        return
    if type(l2) != list:
        print("ERROR in smallestSum(): Recieved non-list value for second input.")
        return
    # The actual Function
    sums = []
    for i in range(len(l1)):
        sums.append(l1[i]+l2[i])
    sums.sort()
    return sums[0]


####    Function Calls    ####
print("****** Result of stringSlicer() ******")
print(stringSlicer("")
print("****** Result of stringChanger(12) ******")
print(stringChanger("change"))
l1 = [0,1,8,12,65,34534]
l2 = [120,2,4,55,323,12]
print("****** Result of smallestSum() ******")
print(smallestSum(l1,l2))