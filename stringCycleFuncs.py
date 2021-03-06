#Takes a string _s and returns a list of all of the cyclical shifts of _s
def stringCyclicShift(_s):
    shifts = []
    sLength = len(_s)

    for i in range(sLength):
        shifts.append(_s[i:sLength]+_s[0:i])

    return(shifts)


#Returns Boolean indicating whether string _s is a palindrome
def isPalindrome(_s):
    palindromic = True
    length = len(_s)

    #even-lengthed palindromes match all the way across, odd-lengthed ones have whatever character in the middle.
    #int(x) automatically floors x, so we don't have to worry about comparing the middle element.
    for i in range(int(length/2)):
        if not(_s[i] == _s[-i-1]):
            palindromic = False

    return(palindromic)



#Wrapper function to remove duplicate string permutations
def allStringPermutations(_s, _maxIndex, _i=0):
    return list(set(allStringPermutationsRec(list(_s), _maxIndex, _i)))

#Takes a list of a string _s and returns a list of all of the permutations of _s
#   _maxIndex is len(_s)-1, and _i is the first index from which to permute
def allStringPermutationsRec(_sList, _maxIndex, _i=0):
    if _i == _maxIndex:
        return(''.join(_sList))
    else:
        activePerms = []
        for j in xrange(_i,_maxIndex+1):
            _sList[_i], _sList[j] = _sList[j], _sList[_i]
            x = allStringPermutationsRec(_sList, _maxIndex, _i+1)

            #Add to the running list differently depending on whether or not
            #   we just got a 'final' value in the recursion.
            if isinstance(x,list):
                activePerms += x
            else:
                activePerms.append(x)

            _sList[_i], _sList[j] = _sList[j], _sList[_i] # backtrack
        return(activePerms)
