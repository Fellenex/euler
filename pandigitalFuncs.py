pandigitalBase = 9

#determines if a single number has any overlapping digits
def isValidMult(_number, _pandigitality=pandigitalBase, _noZeroesAllowed = True):
    strN = str(_number)
    validity = True
    if '0' in strN and _noZeroesAllowed:
        validity = False
    else:
        try:
            cL = countList(_number, _pandigitality, _noZeroesAllowed)
            for n in cL:
                #if we have more than 1 of a digit, or 0 of a digit, then it is not pandigital
                if n > 1 or n == 0:
                    validity = False
        except IndexError:
            validity=False

    return(validity)

#This function can be used on numbers containing 0s, but by default assumes that numbers go from 1..n
#This function can be used on ranges other than 1..n (or 0..n), but then the base must be supplied
def countList(_number, _pandigitality=pandigitalBase, _noZeroesAllowed=True):
    strN = str(_number)
    if _noZeroesAllowed:
        cList = [0]*_pandigitality
        for n in strN:
            cList[int(n)-1] += 1
    else:
        cList = [0]*(_pandigitality+1)
        for n in strN:
            cList[int(n)] += 1      #we don't want to offset the 1-counting to the 0-index if we include zeroes in pandigitality

    return(cList)


#Wrapper for countList which takes a list of digits instead of a single number
def countListFromList(_list, _pandigitality=pandigitalBase, _noZeroesAllowed=True):
    s = ""
    for i in _list:
        s += str(i)

    #We cheat by supplying a string instead of an integer, since that cast may remove leading 0s
    return(countList(s, _pandigitality, _noZeroesAllowed))


#determines if a list of numbers has any overlapping digits
def isValidSequence(_numbers, _pandigitality=pandigitalBase, _noZeroesAllowed=True):
    validity = True
    for n in countListMulti(_numbers, _pandigitality, _noZeroesAllowed):
        #make sure each digit has been used exactly once
        if n > 1 or n == 0:
            validity = False
    return(validity)


#Takes a list of integers and creates a count list for the digits of each
def countListMulti(_numbers, _pandigitality=pandigitalBase, _noZeroesAllowed=True):
    cLists = []
    for n in _numbers:
        cLists.append(countList(n,_pandigitality,_noZeroesAllowed))

    #merge the counts of all the lists by index
    fList = [0]*pandigitalBase
    for i in range(len(cLists)):
        for j in range(pandigitalBase):
            fList[j] += cLists[i][j]

    return(fList)


#Takes a list of numbers and returns true/false depending on whether they all contain the exact same digits
def numbersContainSameDigits(_numbers, _pandigitality=pandigitalBase, _noZeroesAllowed=True):
    cLists = []
    for n in _numbers:
        cLists.append(countList(n,_pandigitality,_noZeroesAllowed))


    sameDigits = True
    for i in range(len(cLists[0])):
        activeValue = cLists[0][i]
        for c in cLists:

            #if the number of 'i's doesn't match up across all lists,
                #then the list doesn't contain rearrangements of the same number
            if not(c[i] == activeValue):
                sameDigits = False
    return(sameDigits)
