"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.


The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

from primeFuncs import gcd, findFactors

#TODO Problem: recurses far too much on numbers like 1.41666666666666... because it uses the length as the magnitude.

#Get the _nth step of the sequence that approximates the square root of 2
def squareRootTwoRecursivePart(_n):
    if _n <= 0:
        exit("ERROR: undefined for n <= 0")
        return(-1)
    elif _n == 1:
        return(0.5)
    else:
        return(1.0 / (2 + squareRootTwoRecursivePart(_n - 1)))


#Takes two integers and returns a tuple of integers with the reduced form _a / _b
def reduceFraction(_a, _b):
    frac = (_a, _b)
    factor = gcd(_a, _b)
    while not(factor == 1):
        frac = (frac[0] / factor, frac[1] / factor)
        factor = gcd(frac[0], frac[1])

    return(frac)

#Takes a decimal number and returns a tuple of some (not necessarily reduced) form of this fraction
def fractionFromDecimal(_dec):
    length = len(str(_dec)) - 2     #the number of post-decimal places
    mag = pow(10,length)

    #print("Sending %d / %d to reduction" % (_dec * mag, mag))
    #return(reduceFraction(_dec * mag, mag))

    return(_dec * mag, mag)

for i in range(1,4):
    x = 1 + squareRootTwoRecursivePart(i)
    y = fractionFromDecimal(x)

    print(x)
    print(gcd(y[0],y[1]))
    #print(findFactors(y[0]))
    #print(findFactors(y[1]))

    print()
    #print(fractionFromDecimal(x))
