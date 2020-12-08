"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from pandigitalFuncs import *


divisibilityChecks = [2,3,5,7,11,13,17]
indexTuples = [(1,4), (2,5), (3,6), (4,7), (5,8), (6,9), (7,10)]
haveDivisibilityProperty = []

pandigitalStrings = generateAllPandigitals(pandigitalBase, False)

assert(len(divisibilityChecks) == len(indexTuples))
for p in pandigitalStrings:

    #start the counter to see how many of the numbers we get through.
    #we start from the end because the larger primes have fewer multiples, so we eliminate more checks earlier.
    i = len(indexTuples) - 1

    #loop through each index of divisibility check.
    while i >= 0 and int(p[indexTuples[i][0] : indexTuples[i][1]]) % divisibilityChecks[i] == 0:
        i -= 1

    #every segment is divisible by the proper numbers.
    if i == -1:
        haveDivisibilityProperty.append(int(p))


print(haveDivisibilityProperty)
print(sum(haveDivisibilityProperty))
