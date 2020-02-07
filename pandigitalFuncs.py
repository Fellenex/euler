pandigitalNum = 9

#determines if a single number has any overlapping digits
def isValidMult(_number, _pandigitality=pandigitalNum):
    strN = str(_number)
    validity = True
    if '0' in strN:
        validity = False
    else:
        try:
            cL = countList(_number, _pandigitality)
            for n in cL:
                if n > 1 or n == 0:
                    validity = False
        except IndexError:
            validity=False
            
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
def countList(_number, _pandigitality=pandigitalNum):
    cList = [0]*_pandigitality
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
