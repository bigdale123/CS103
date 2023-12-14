# Lab 3 UNGRADED exercises
# These exercises are for practice only
# In order to get attendance grade, you should complete the functions and return this file

def stringSlicer(s1):
    return s1[-4:]

def tupleCounter(t1,s2):
    return t1.count(s2)


def listSorter(l1):
    l1.sort()
    return l1
    




########################################################
# Function Calls
########################################################

print ("\n**************************************")
s1 = "UAB CS103 LAB3"		
print ("The result of stringSlicer")
print(stringSlicer(s1))
print ("\n**************************************")

t1= ("u", "a", "b", "u", "s", "a", "c", "s")
s2 = "a"
print ("The result of tupleCounter")
print(tupleCounter(t1,s2))
print ("\n**************************************")


l1 = [2, 5, 3, 1, 9, 5]	
print ("The result of listSorter ")
print(listSorter(l1))   
print ("\n**************************************")

