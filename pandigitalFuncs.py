pandigitalNum = 9

#determines if a single number has any overlapping digits
def isValidMult(_number, _pandigitality=pandigitalNum, _noZeroesAllowed = True):
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

#This function shouldn't be used on numbers containing 0s, since we are only looking to count integers from 1..n
def countList(_number, _pandigitality=pandigitalNum, _noZeroesAllowed=True):
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


#determines if a list of numbers has any overlapping digits
def isValidSequence(_numbers):
    validity = True
    for n in countListMulti(_numbers):
        #make sure each digit has been used exactly once
        if n > 1 or n == 0:
            validity = False
    return(validity)

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
