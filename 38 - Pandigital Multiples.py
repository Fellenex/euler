"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying
    by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
    which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be
    formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from pandigitalFuncs import isValidMult
from stringCycleFuncs import allStringPermutations

#(1,2,3,4,5,6,7,8,9) can only work for n=1
#(1,2,3,4,5,6,7,8) cannot work for any n
#(1,2,3,4,5,6,7) cannot work for any n
#(1,2,3,4,5,6) can only work for n=3
#(1,2,3,4,5) can only work for 5 <= n <= 9
#(1,2,3,4) can only work for 25 <= n <= 33
#(1,2,3) can only work for 100 <= n <= 333
#(1,2) can only work for 5000 <= 9999

#gets the relevant n ranges for each (1,...,n) multiple range
rangeDict = {}
for r in range(2,10):
    mi = float('inf')
    ma = 0
    for n in range(1,10000):
        test = ""
        for x in range(1,r):
            test += str(n*x)

        if len(test)==9:
            mi = min(mi,n)
            ma = max(ma,n)

    if not((mi,ma) == (float('inf'),0)):
        #rangeDict[r] represents the possible n values for range(1,r)
        rangeDict[r-1] = (mi,ma+1)


maxPanConcatenation = 0
for r in rangeDict:
    for i in range(rangeDict[r][0],rangeDict[r][1]):
        currStr = ""
        for j in range(1,r+1):
            currStr += str(i*j)

        if isValidMult(int(currStr)):
            print(currStr+" is a pandigital concatenation, starting with "+str(i)+" and using range [1,"+str(r)+"]")
            maxPanConcatenation = max(maxPanConcatenation, int(currStr))

print(maxPanConcatenation)
exit()


#This version takes ~735 seconds to run.

pandigitalNumbers = [int(x) for x in allStringPermutations("123456789",8)]
multipleSets = [range(1,x) for x in range(2,11)]

#We only need to go up to 9999, since 9999 . (9999*2) is the largest 9-digit number
maxPanConcatenation = 0
for i in range(1,10000):
    for r in multipleSets:
        currStr = ""
        for j in r:
            currStr += str(i*j)

        if int(currStr) in pandigitalNumbers:
            print(currStr+" is a pandigital concatenation, starting with "+str(i)+" and using range "+str(r))
            if int(currStr) > maximal: maximal = int(currStr)

        if len(currStr) > 9:
            break

print(maximal)
