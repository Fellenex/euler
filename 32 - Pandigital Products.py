"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from pandigitalFuncs import *

#a x b = c

min = 2     #if a is 1 then c=b (and vice versa), therefore c isn't pandigital
max = 4987  #largest pandigital multiplicand/multiplier whose product can still be fewer than 5 digits
#neither a nor b can be 5 digits (or longer), because then a x b = c contains at least 11 digits (and therefore isn't pandigital)


validSequences = {}
#first, find a possible a value
for a in range(min,max):
    if isValidMult(a):

        #then, find a value for b which doesn't overlap with a
        for b in range(min,max):
            if isValidMult(b):

                #c has to be below 9877 to not have too many (or any repeated) digits
                c = a*b
                if c < 9877 and isValidMult(c):
                    if isValidSequence([a,b,c]):
                        #we don't want to include the same product multiple times,
                        #so we can just set this key's value to 1 everytime
                        validSequences[c] = 1
print(validSequences)

answer = 0
for key in validSequences:
    answer += key

print(answer)
