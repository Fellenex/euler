"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import math
from pandigitalFuncs import numbersContainSameDigits

testRanges = [100,1000,10000,100000,1000000]
multiples = [2,3,4,5,6]

for i in range(1, len(testRanges)):
    upperEnd = int(math.floor(testRanges[i]/6))

    for j in range(testRanges[i-1], upperEnd+1):
        relevantMultiples = [j] + [j*m for m in multiples]
        if numbersContainSameDigits(relevantMultiples):
            print("The smallest positive integer x s.t. each multiple of x by "+str(multiples)+" contains the same digits is "+str(j))
            print(relevantMultiples)
            exit()
