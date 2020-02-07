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


divisibilityTriples = [2,3,5,7,11,13,17]
indexTriples = [(2,4), (3,5), (4,6), (5,7), (6,8), (7,9), (8,10)]

pandigitalNumbers = []

#These numbers are too large to iterate through, discovering pandigitality (re: time taken to do so)
#Instead, TODO: they need to be generated using permutations.
n = 1023456789
while n <= 9876543210:
    if isValidMult(n, 9, False):
        pandigitalNumbers.append(n)
    n+=1

print(pandigitalNumbers)
exit()

for p in pandigitalNumbers:
    for i in range(7):
        sP = str(p)[indexTriples[i][0]-1:indexTriples[i][1]]
