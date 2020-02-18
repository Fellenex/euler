"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import math


#Converts a decimal number _n into a binary string with the smallest number of bits.
def decimalToBinary(_n):
    if _n == 0 or _n == 1:
        return(str(_n))
    elif _n == 2:
        return("10")
    else:
        power = int(math.floor(math.log(_n, 2)))
        remaining = _n
        bString = ''

        #Successively remove the largest power of 2 that we can from the remaining integer
        for i in range(power, -1, -1):
            if remaining >= math.pow(2,i):
                remaining -= math.pow(2,i)
                bString += '1'
            else:
                bString += '0'

        return(bString)


#Increases a binary number _b's length to be _desiregLength-many characters long
def padBinaryNumber(_b, _desiredLength):
    bLength = len(_b)
    if bLength > _desiredLength:
        print("ERROR: "+_b+" already has length "+str(len(_b))+" and was requested to be padded to "+str(_desiredLength))
        return("-1")
    elif bLength == _desiredLength:
        return(_b)
    else:   #len(_b) < _desiredLength
        prefix = '0' * (_desiredLength - bLength)
        return(prefix+_b)

def isPalindrome(_s):
    palindromic = True
    length = len(_s)

    #even-lengthed palindromes match all the way across, odd-lengthed ones have whatever character in the middle.
    #int(x) automatically floors x, so we don't have to worry about comparing the middle element.
    for i in range(int(length/2)):
        if not(_s[i] == _s[-i-1]):
            palindromic = False

    return(palindromic)


#We have to check up to 1'000'000, whose binary number has a length of 20.
#So then we will pad everything to 20
doublePalindromeSum = 0
target = 1000000
targetBinaryLength = 20


for i in range(1,target):
    #Get the binary version of i, and remove leading 0s,
    if isPalindrome(str(i).lstrip('0')) and isPalindrome(padBinaryNumber(decimalToBinary(i),targetBinaryLength).lstrip('0')):
        doublePalindromeSum += i

print("The sum of all base-10 and base-2 palindromes below "+str(target)+" is "+str(doublePalindromeSum))
