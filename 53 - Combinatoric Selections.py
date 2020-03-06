"""
How many, not necessarily distinct,
    values of (n \choose r) for 1 <= n <= 100, are greater than one-million?
"""

from combinatoricFunctions import *
import math

chooseMemos = dict()
targetValue = 1000000
relevantPairs = []

for n in range(1,101):
    factMemos[n] = memoizedFactorial(n)

    for r in range(1,int(math.floor(n/2.0))+1):
        activeValue = nCr(n,r)
        chooseMemos[(n,r)] = activeValue
        chooseMemos[(n,n-r)] = activeValue

        if activeValue > targetValue:
            relevantPairs.append((n,r))
            if not(n-r == r):
                relevantPairs.append((n,n-r))


print(relevantPairs)
print("There are "+str(len(relevantPairs))+" pairs (n,r) where 1<=r<=n<=100 such that (n choose r) > 1000000")
