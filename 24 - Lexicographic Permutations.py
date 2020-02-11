"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math


availableDigits = [0,1,2,3,4,5,6,7,8,9]
total = []
targetPermutation = 1000000
runningBalance = 0

#Out of n! permutations, the first (n-1)! of them will start with 0, the second (n-1)! will start with 1, etc
#Once we've fonud the first digit, then we can reiterate starting with (n-1)! permutations counting up in sets of (n-2)!
for p in range(9,-1,-1):
    currentDigit = 0
    perDigit = math.factorial(p)
    while runningBalance + perDigit < targetPermutation:
        print("Going from "+str(runningBalance)+" to "+str(runningBalance + perDigit)+" on the "+str(10-p)+"th digit")
        runningBalance += perDigit
        currentDigit += 1

    #Remove the element from the list, since we aren't allowing repetitions in these permutations.
    total.append(availableDigits[currentDigit])
    availableDigits.remove(availableDigits[currentDigit])

print(total)
