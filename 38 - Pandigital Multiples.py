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

pandigitalNumbers = [int(x) for x in allStringPermutations("123456789",8)]
multipleSets = [range(1,x) for x in range(2,11)]

print(len(pandigitalNumbers))

#This version takes ~735 seconds to run.
#We only need to go up to 9999, since 9999 . (9999*2) is the largest 9-digit number
maximal = 0
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

#print(allStringPermutations("1234",3))
