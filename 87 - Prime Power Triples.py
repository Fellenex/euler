"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

from primeFuncs import sieve_of_atkin
import math


#7072^2 is already larger than 50'000'000, so we don't need primes higher than that.
primes = sorted(sieve_of_atkin(7072))


target = 50000000
expressables = set()       #can't just use a counter, because some numbers could be found in different ways

#smallest square is 2^2, largest square is 7071^2
primeSquares = [p*p for p in primes if p < math.ceil(target ** (1/2.0))]

#smallest cube is 2^3, largest cube is 368^3
primeCubes = [p*p*p for p in primes if p < math.ceil(target ** (1/3.0))]

#smallest fourth is 2^4, largest fourth is 84
primeFourths = [p*p*p*p for p in primes if p < math.ceil(target ** (1/4.0))]


for s in primeSquares:
    for c in primeCubes:
        for f in primeFourths:

            if s+c+f < target:
                expressables.add(s+c+f)


print(len(expressables))
