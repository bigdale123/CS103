#################################################
#  Name: Dylan Calvin
#  BlazerID: dylcal13
#  Assignment: Lab 5 (Ungraded)
#################################################

def starLine(n):
    # Error Trapping
    if type(n) != int:
        print("ERROR in starLine(): Recieved non-int value for input.")
        return

    # The actual function
    for i in range(1,n+1):
        print("*"*i)

def cashier(c):
    # Error Trapping
    if type(c) != int:
        print("ERROR in cashier(): Recieved not-int value for input.")
        return ""

    # The actual function
    total = 0
    for i in range(1,c+1):
        print("For Item "+str(i))
        price = float(input(" -Enter Price of Item "+str(i)+": "))
        tax = float(input(" -Enter Tax Rate of Item "+str(i)+": "))
        total += price+(price*(tax/100))
    return ("Total Cost of purchases: $"+str(total))

def stringPair(s1,s2):
    # Error Trapping
    if type(s1) != str:
        print("ERROR in stringPair(): Recieved non-string value for first input.")
        return
    if type(s2) != str:
        print("ERROR in stringPair(): Recieved non-string value for second input.")
        return
    
    # The actual function
    for i in range(len(s1)):
        print(s1[i],s2[i])


#######        Function Calls        #######
print("****** Result of starLine(5) ******")
print()
starLine(5)
print()
print("****** Result of cashier(c) ******")
print(cashier(2))
print()
print("***** Result of stringPair(\"abc\",\"xyz\") ******")
stringPair("abc","xyz")