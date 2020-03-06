"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from primeFuncs import sieve_of_atkin,checkPrimeEfficiently

#Returns Boolean deciding whether the concatenation of strings _x_y and _y_x are both prime
def primeConcats(_x,_y):
    return (checkPrimeEfficiently(int(_x + _y))) and (checkPrimeEfficiently(int(_y + _x)))

maxPrime = 10000
primes = sieve_of_atkin(maxPrime)
numPrimes = len(primes)
primes.sort()

#This seems kind of hacky but maybe it's still the best way?
#It works pretty quickly for the 4-prime version.
minimalSum = float('inf')
for a in range(0, numPrimes):
    sA = str(primes[a])

    for b in range(a+1, numPrimes):
        sB = str(primes[b])

        if primeConcats(sA,sB):
            for c in range(b+1, numPrimes):
                sC = str(primes[c])

                if primeConcats(sA,sC) and primeConcats(sB,sC):
                    for d in range(c+1, numPrimes):
                        sD = str(primes[d])

                        if primeConcats(sA,sD) and primeConcats(sB,sD) and primeConcats(sC,sD):
                            for e in range(d+1, numPrimes):
                                sE = str(primes[e])

                                if primeConcats(sA,sE) and primeConcats(sB,sE) and primeConcats(sC,sE) and primeConcats(sD,sE):
                                    minimalSum = min(minimalSum, sum([primes[a],primes[b],primes[c],primes[d],primes[e]]))
                                    print(minimalSum)
                                    print(sA,sB,sC,sD,sE)
                                    exit("Finished!")
