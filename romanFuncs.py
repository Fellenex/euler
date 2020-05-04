romanDict = dict()
romanDict["I"] = 1
romanDict["V"] = 5
romanDict["X"] = 10
romanDict["L"] = 50
romanDict["C"] = 100
romanDict["D"] = 500
romanDict["M"] = 1000

#possible pairs: IV, IX, XL, XC, CD, CM

#Takes an integer _n and converts it to the minimally-lengthed roman numeral
def integerToRoman(_n):
    remainder = _n
    numeral = ""

    while remainder >= 1000:
        numeral += "M"
        remainder -= 1000

    if remainder >= 900:
        numeral += "CM"
        remainder -= 900

    if remainder >= 500:
        numeral += "D"
        remainder -= 500
    elif remainder >= 400:
        numeral += "CD"
        remainder -= 400

    while remainder >= 100:
        numeral += "C"
        remainder -= 100

    if remainder >= 90:
        numeral += "XC"
        remainder -= 90

    if remainder >= 50:
        numeral += "L"
        remainder -= 50
    elif remainder >= 40:
        numeral += "XL"
        remainder -= 40

    while remainder >= 10:
        numeral += "X"
        remainder -= 10

    if remainder >= 9:
        numeral += "IX"
        remainder -= 9

    if remainder >= 5:
        numeral += "V"
        remainder -= 5
    elif remainder >= 4:
        numeral += "IV"
        remainder -= 4

    while remainder >= 1:
        numeral += "I"
        remainder -= 1

    assert(remainder == 0)
    return(numeral)


#Takes a roman numeral string _r and converts it into a decimal integer
def romanToInteger(_r):
    i = 0
    runningSum = 0
    recentSubtractive = False   #we only add the last character individually if it didn't occur as part of a subtractive pair

    while i < len(_r)-1:

        if romanDict[_r[i]] < romanDict[_r[i+1]]:
            #_r[i] and _r[i+1] make a subtractive pair
            runningSum += romanDict[_r[i+1]] - romanDict[_r[i]]
            i += 2

            recentSubtractive = True

        else:
            runningSum += romanDict[_r[i]]
            i+=1

            recentSubtractive = False

    #the last character can never occur as the first part of a subtractive pair
    #but if the third and second-last characters were a pair, correct for that here
    if not(recentSubtractive) or i == len(_r)-1:
        runningSum += romanDict[_r[-1]]

    return(runningSum)
