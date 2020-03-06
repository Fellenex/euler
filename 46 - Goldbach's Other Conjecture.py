"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as
    the sum of a prime and twice a square?
"""

from primeFuncs import sieve_of_atkin

numOdds = 75
odds = [(2*n)-1 for n in range(2,numOdds+2)]
oddComposites = []
maxSquare = 51
goldbachPossible = dict()

for i in range(len(odds)):
    for j in range(i,len(odds)):
        oddComposites.append(odds[i]*odds[j])
oddComposites.sort()

primes = sieve_of_atkin(oddComposites[-1])
primes.sort()

for p in primes:
    for s in range(1,51):
        goldbachPossible[p + (2*s*s)] = True

for comp in oddComposites:
    if not(comp in goldbachPossible):
        print(str(comp)+" cannot be created by p + 2*(x^2) for any prime p<="+str(primes[-1])+" and odd composite x<="+str(maxSquare))

exit()

#Old inefficient solution: Takes ~140 seconds to complete.

#Now we want to find the smallest odd composite that cannot be written as the sum of a prime
for comp in oddComposites:
    goldbachConjecture = False
    i = 0
    while primes[i] < comp:

        #try 2*(x^2) for all numbers such that the current prime + 2*(x^2) <= comp
        currDiff = comp - primes[i]

        for j in range(1,currDiff):
            if (primes[i] + (2 * j*j)) == comp:
                goldbachConjecture = True

                #breaks out of inner for-loop, but not the outer while-loop
                break

        #if we already found a solution, then skip to checking the next composite
        if goldbachConjecture:
            break
        else:
            i += 1

    #If no solution was found, then this is the minimal counterexample
    if not(goldbachConjecture):
        print(str(comp)+" cannot be created by p + 2*(x^2) for any prime p and odd composite x")
        exit()
