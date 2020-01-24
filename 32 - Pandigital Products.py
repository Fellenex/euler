"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

#a x b = c
pandigitalNum = 9

min = 2     #if a is 1 then c=b (and vice versa), therefore c isn't pandigital
max = 4987  #largest pandigital multiplicand/multiplier whose product can still be fewer than 5 digits
#neither a nor b can be 5 digits (or longer), because then a x b = c contains at least 11 digits (and therefore isn't pandigital)

#determines if a single number has any overlapping digits
def isValidMult(_number):
    strN = str(_number)
    validity = True
    if '0' in strN:
        validity = False
    else:
        cL = countList(_number)
        for n in cL:
            if n > 1:
                validity = False
    return(validity)

#determines if a list of numbers has any overlapping digits
def isValidSequence(_numbers):
    validity = True
    for n in countListMulti(_numbers):
        #make sure each digit has been used exactly once
        if n > 1 or n == 0:
            validity = False
    return(validity)


#This function shouldn't be used on numbers containing 0s, since we are only looking to count integers from 1..n
def countList(_number):
    cList = [0]*pandigitalNum
    strN = str(_number)
    for n in strN:
        cList[int(n)-1] += 1
    return(cList)


#Takes a list of integers and creates a count list for the digits of each
def countListMulti(_numbers):
    cLists = []
    for n in _numbers:
        cLists.append(countList(n))

    #merge the counts of all the lists by index
    fList = [0]*pandigitalNum
    for i in range(len(cLists)):
        for j in range(pandigitalNum):
            fList[j] += cLists[i][j]

    return(fList)




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
