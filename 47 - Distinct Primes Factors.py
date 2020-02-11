"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 × 23
645 = 3 x 5 × 43
646 = 2 x 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from primeFuncs import uniquePrimeFactorization, sieve_of_atkin


primes = sieve_of_atkin(135000)

window = 1
primeRange = []

for i in range(2,primes[-1]):
    j=i
    while len(set(uniquePrimeFactorization(j))) > window:
        j+= 1

    j -=1   #compensate for the last addition that was made

    if j-i >= window:
        window = j-i+1
        primeRange = (i, j)
        print("Prime range "+str(primeRange)+" has a window of size "+str(window)+" with "+str(window)+" unique factors each")

    i=j

print(window)
print(primeRange)
