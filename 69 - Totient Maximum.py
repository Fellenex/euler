"""
Euler's Totient function, phi(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.

It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""

from primeFuncs import coprime, sieve_of_atkin, uniquePrimeFactorization, gcd
import math

miniTarget = 1000
target = 1000000
maximumTotient = 0
maximumTotientCauser = 0

primes = sorted(sieve_of_atkin(miniTarget))

for i in range(2,miniTarget+1):
    if not(i in primes):
        #all numbers are relatively prime to 1
        t = 1

        for j in range(2,i):
            if coprime(i,j):
                t += 1

        if i / (t*1.0) > maximumTotient:
            maximumTotient = i / (t*1.0)
            maximumTotientCauser = i

#By inspection, the totient maximums for <=10, <=100, and <=1000 are 6, 30, and 210
#These are 2*3, 2*3*5, and 2*3*5*7
print("The maximum totient for n <= "+str(miniTarget)+" is "+str(maximumTotient)+", caused by "+str(maximumTotientCauser))

#Assumption: the number with the largest totient is a product of unique primes

#Get the largest product of unique primes still lower than our target
p = 0
targetProduct = 1
while targetProduct * primes[p] < target:
    targetProduct *= primes[p]
    p += 1

primeFactorization = primes[:p]
rangeList = set(range(1,targetProduct))
for f in primeFactorization:
    i = 1
    while i*f < targetProduct:
        #print("Removing "+str(i*f)+" from "+str(targetProduct))
        if i*f in rangeList:
            rangeList.remove(i*f)
        i += 1
print("The largest product of unique primes below "+str(target)+" is "+str(targetProduct)+", which has phi(n)="+str(len(rangeList))+" and n/phi(n)="+str(targetProduct/(len(rangeList)*1.0)))

for t in rangeList:
    try:
        assert(coprime(t,targetProduct))
    except AssertionError:
        print("Oops", t, targetProduct)
