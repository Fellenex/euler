"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
    exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from pandigitalFuncs import countList
from primeFuncs import checkPrimeEfficiently


maxVal = 10000

for i in range(1000,maxVal):
    if i%1000 == 0: print(i)
    for j in range(1,int(((maxVal-i)*1.0)/2)):

        #Create the three numbers between [1000,9999] that have equal difference
        currSet = [i, i+j, i+j+j]
        counts = [countList(x, 9, False) for x in currSet]
        #if the numbers are permutations of each other (i.e., they have the same digit count for each digit)
        if counts[0] == counts[1] and counts[0] == counts[2]:

            #if all of the numbers are prime
            if checkPrimeEfficiently(currSet[0]) and checkPrimeEfficiently(currSet[1]) and checkPrimeEfficiently(currSet[2]):
                print("Valid prime permutations with equal difference: "+str(currSet))
