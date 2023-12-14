def hailstone(n2):

    while n2 > 1:
        if n2%2 == 0:
            n2 /= 2
        else:
            n2 *= 3
            n2 += 1
        #This is just for formatting
        if n2 == 1:
            print(int(n2))
        else:
            print(int(n2), end=", ")

def keysToRemove(d1,l1):
    for i in l1:
        d1.pop(i, None)
    return d1

def animalLegs(d2):
    legs = 0
    for i in d2.keys():
        if i == "chickens":
            legs += d2[i]*2
        else:
            legs += d2[i]*4
    return legs

hailstone(3)
hailstone(6)
hailstone(7)

print(keysToRemove({"FirstName": "Mark","LastName":"Zuckerberg","Salary":2000000,"City": "Palo Alto","Company":"Facebook"},["Salary","Company"]))

print(animalLegs({"chickens":10,"rabbits":5}))
print(animalLegs({"dogs":10,"chickens":5,"cows":5}))
