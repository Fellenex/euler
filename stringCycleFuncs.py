#Takes a string _s and returns a list of all of the cyclical shifts of _s
def stringCyclicShift(_s):
    shifts = []
    sLength = len(_s)

    for i in range(sLength):
        shifts.append(_s[i:sLength]+_s[0:i])

    return(shifts)
