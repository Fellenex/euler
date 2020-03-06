"""
The number, 197, is called a circular prime because all rotations
    of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from primeFuncs import sieve_of_atkin_set
from stringCycleFuncs import stringCyclicShift

primes = sieve_of_atkin_set(1000000)
circularPrimes = []

for p in primes:
    circular = True

    #Create all of the cyclic shifts for the current prime
    for cs in stringCyclicShift(str(p)):

        #If even one of the shifts isn't prime, then the prime isn't circular
        if not(int(cs) in primes):
            circular = False

    if circular:
        circularPrimes.append(p)

print(circularPrimes)
print(len(circularPrimes))
