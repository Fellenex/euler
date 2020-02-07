"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from primeFuncs import sieve_of_atkin
from pandigitalFuncs import *

#In theory there could be a 9-digit pandigital prime, but memory runs out when
#   moving from 8 digits to 9 digits. Luckily the largest is only 7 digit pandigital.
upperBound = 10000000
primes = sieve_of_atkin(upperBound)
primes.sort()
primes.reverse()

for p in primes:
    if isValidMult(p, len(str(p))):
        print(str(p)+" is the largest pandigital prime below "+str(upperBound))
        break
