"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

from combinatoricFunctions import *


#For digits of _n = n1 .. nk, gets (n1)! + ... + (nk)!
def sumDigitsFactorials(_n):
    factorialSum = 0
    for c in str(_n):
        factorialSum += memoizedFactorial(int(c))

    return factorialSum


#memoize chain lengths since they all seem to return
chainLengthDict = dict()
numMemoized = 0
targetLength = 60
numChainsCorrectLength = 0

y =[169, 69, 1454, 145, 540]
#for x in y:
for x in range(1,100):



    """
    #if the first factorialized digit is already memoized, don't bother with the loop
    if recentDigit in chainLengthDict:
        if chainLengthDict[recentDigit] == targetLength:
            numChainsCorrectLength += 1

        numMemoized += 1

        chainLengthDict[x] = chainLengthDict[recentDigit]
        print("\tadded "+str(chainLengthDict[recentDigit])+" to "+str(x)+" as length: "+str(chainLengthDict[x]))
        print()

    else:
    """

    cycleDigits = [x]
    recentDigit = sumDigitsFactorials(x)

    #print("\t"+str(x)+","+str(recentDigit))
    memoFound = False

    #until we reach a number that we haven't yet found, keep track of the summing the digits' factorials
    while not(recentDigit in cycleDigits):
        #print("\t\t"+str(recentDigit))

        #if we've already memoized this new number, then save the work of going through the loop
        if not(recentDigit in chainLengthDict):
            #print("adding "+str(sumDigitsFactorials(recentDigit)))
            cycleDigits.append(recentDigit)
            recentDigit = sumDigitsFactorials(recentDigit)

        else:
            if len(cycleDigits) + chainLengthDict[recentDigit] == targetLength:
                numChainsCorrectLength += 1

            numMemoized += 1
            memoFound = True

            if chainLengthDict[recentDigit] == 1:
                chainLengthDict[x] = len(cycleDigits) + 1
            else:
                chainLengthDict[x] = len(cycleDigits) + chainLengthDict[recentDigit] - 1
            print("\taddedy "+str(len(cycleDigits))+"+"+str(chainLengthDict[recentDigit])+"-1 to "+str(x)+" as length: "+str(chainLengthDict[x]))
            break



    if not(memoFound):
        chainLengthDict[x] = len(cycleDigits)
        print("\taddedx "+str(len(cycleDigits))+" to "+str(x)+" as length: "+str(chainLengthDict[x]))

        chainLengthDict[recentDigit] = len(cycleDigits) - cycleDigits.index(recentDigit)
        print("\taddedz "+str(chainLengthDict[recentDigit])+" to "+str(recentDigit)+" as length")

        if len(cycleDigits) == targetLength:
            numChainsCorrectLength += 1

    print("\t"+str(cycleDigits))
    print()


print("Saved calls "+str(numMemoized)+" times")
#print(cycleDigits)
#print(len(cycleDigits))
print(numChainsCorrectLength)
print(chainLengthDict)

#for c in chainLengthDict:
    #print(c,chainLengthDict[c])
