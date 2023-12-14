# Lab 3 GRADED exercises
# Return only this script file

def listInsert (l2,x):
    l2.insert(-1,x)
    l2.sort()
    l2.reverse()
    return l2
    
# define mailingCost HERE 
def mailingCost (d):
    if d <= 50:
        cost = d*5.00
    elif d >= 51 and d <= 200:
        cost = d*4.25
    elif d >= 201 and d <= 500:
        cost = d*3.95
    elif d >= 501:
        cost = d*3.70
    return cost

#define  str2tuple HERE
def str2tuple (s3,s4):
    newstr = s3+s4
    return tuple(newstr)

#define  tupleLast3 HERE 
def tupleLast3 (t2):
    assert len(t2) >= 4
    return t2[-3]


########################################################
# Function Calls
########################################################

print ("\n**************************************")
l2 = [2, 5, 7, 8, 11]		
x = 6
print ("The result of listInsert ")
print(listInsert (l2,x))
print ("\n**************************************")

print ("The result of mailing cost calculation ")
d=200
print(mailingCost(d))
print ("\n**************************************")

s3 = 'Hello'
s4 = "World"
print ("The result of str2tuple ")
print(str2tuple(s3,s4))
print ("\n**************************************")

t2 = ("u", "a", "b", "2", "3", "4", "c", "i", "s")
print ("The result of tupleLast3 ")
print(tupleLast3(t2))
print ("\n**************************************")