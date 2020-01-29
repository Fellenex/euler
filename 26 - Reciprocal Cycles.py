import decimal

#TODO: findStringCycle(s) doesn't account for cycles like (100), where 0->0 and 0->1.
#   Problem: it assumes that each next letter must be unique.
#   Potential solution: so long as the first character hasn't been rereached,
#       keep track of the "ongoing cyclical string".
#   Have to be careful though, because a cycle like (10102) would also be valid,
#       and this reaches the first character in the middle.
#   We also have to consider that there is some initial part where
#       the cycle has yet to start, as in 1/6 = 0.1(6)
#       As it currently stands, the function says 1/6 has cycle length 2 (number of elements in dictionary)

#Returns the length of the cycle in s (if s is cyclical)
#Returns -1 otherwise
def findStringCycle(s):
    cycleValues = {}
    cyclicity = True

    #For each letter c, create a function f(c) whose value is the next character.
    #If we run into multiple assignments for f(c), then it can't be a cycle.
    for c in range(len(s)-1):
        try:
            if not(cycleValues[s[c]] == s[c+1]):
                #print(s[c]+"->"+s[c+1]+" broke the cycle for "+str(s))
                cyclicity = False
                break
        except KeyError:
            cycleValues[s[c]] = s[c+1]

    if cyclicity:
        print("String "+s+" has cycle"+str(cycleValues))
        return(len(cycleValues))
    else:
        return(-1)


specialOne = decimal.Decimal(1.0)
maxDecimals = 0
unitFractions = []

#Calculate all of the unit fractions from 1/2 to 1/999, and find the longest one.
for i in range(2,10):
    x = decimal.Decimal(specialOne/i)
    unitFractions.append(x)

    numLength = len(str(x))
    maxDecimals = max(maxDecimals,numLength)


#Find which unit fraction causes the largest cycle
maxCycleLength = 0
maxCycleCauser = 0
for i in range(2,10):
    #unitFractions[i-2] to offset that we don't have 1/0 or 1/1
    #[2:] to throw away the prefixing "0."
    activeDecimals = str(unitFractions[i-2])[2:]

    #Only bother considering the longest strings
    #Offset by -2 to account for the removed "0."
    if len(activeDecimals) == maxDecimals-2:

        #[:-1] to throw away any rounding that might be happening
        print(activeDecimals[:-1])
        currCycleLength = findStringCycle(activeDecimals[:-1])

        if currCycleLength > maxCycleLength:
            maxCycleLength = currCycleLength
            maxCycleCauser = i

print("1/"+str(maxCycleCauser)+" has a decimal cycle of length "+str(maxCycleLength))
