"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.


The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

from fractions import Fraction

EXPANSION_SIZE = 1000
MEMOIZED_EXPANSION = [0] * (EXPANSION_SIZE+1)
MEMOIZED_EXPANSION[1] = Fraction(0.5)


#Get the _nth step of the sequence that approximates the square root of 2
def squareRootTwoRecursivePart(_n):

    #Store previously unknown fractions so that we don't have to recurse too deeply
    if MEMOIZED_EXPANSION[_n] == 0:
        MEMOIZED_EXPANSION[_n] = Fraction(1 / (2 + squareRootTwoRecursivePart(_n - 1)))

    _n = Fraction(_n)

    if _n <= 0:
        exit("ERROR: undefined for n <= 0")
        return(-1)

    else:
        return(MEMOIZED_EXPANSION[int(_n)])


#Counts the number of fractions where the numerator has more digits than the denominator
topHeavyFractionCount = 0
for i in range(1,1001):
    x = 1 + squareRootTwoRecursivePart(i)

    if len(str(x.numerator)) > len(str(x.denominator)):
        topHeavyFractionCount += 1


print(topHeavyFractionCount)
