"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

import math
import decimal

perfectSquares = [i*i for i in range(1,11)]
print(perfectSquares)


digitalSum = 0

for i in range(1,100):
    if not(i in perfectSquares):
        x = decimal.Decimal(math.sqrt(i))
        print(len(str(x)))

print(format(math.sqrt(2), '.60f'))

#x = math.sqrt(2) * 2 ** 55
#print((x * 10 ** 55) // (2 ** 55))

z = 1.4142135623730951454746218587388284504413604736328125
print(z)
zP = decimal.Decimal(str(z)+"1")
zM = decimal.Decimal(str(z)[:-1]+"4")
print(zP*zP)
print(zM*zM)
