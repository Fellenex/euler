"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""

from primeFuncs import coprime, uniquePrimeFactorization
import time

def repunit(_n):
    return(int('1'*_n))



leastExceeder = 0
increments = [2,4,2,2]  #Rather than checking for coprimality between n and 10, we can use any number ending in 1, 3, 7, or 9.
maxSoFar = 0
maxDict = dict()

n = 1
i = 0       #index for increments
while (leastExceeder == 0):
    k = 0
    while True:
        k += 1
        if repunit(k) % n == 0:
            print("R(%d) is divisible by %d" % (n, k))

            if k > maxSoFar:
                maxSoFar = k
                maxDict[n] = k

            if k > 100:
                leastExceeder = (n,k)

            break

    n += increments[i]
    i = (i+1)%4

print([(key,uniquePrimeFactorization(maxDict[key])) for key in maxDict])
print(leastExceeder)

x = repunit(7)
print(x%6)
