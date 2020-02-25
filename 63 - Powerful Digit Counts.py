"""
The 5-digit number, 16807=75, is also a fifth power.
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


#Getting math overflow errors using math.pow
def myPow(_base, _pow):
    p = _pow
    r = _base
    while p > 1:
        r *= _base
        p -=1
    return(r)


#There are 9 integers n s.t. n^1 has 1 digit
powerCountMatches = range(1,10)

for power in range(2,1000):
    activeBase = 1
    activeResult = 1
    while activeResult < myPow(10, power):
        activeResult = myPow(activeBase, power)
        sA = str(activeResult)
        #print(sA+" is "+str(activeBase)+"^"+str(power)+" and has length "+str(len(sA)))
        if len(sA) == power:
            powerCountMatches.append(activeResult)

        activeBase += 1

print(len(powerCountMatches))
print(powerCountMatches)
