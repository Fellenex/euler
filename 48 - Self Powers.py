"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

from genericMathFuncs import myPow

selfPowers = [myPow(i,i) for i in xrange(1,1001)]
selfPowerSuffixes = []

#Since we only need the final 10 characters of the total sum,
#   then getting the final (up to) 10 characters of each
#   element of the series is more than sufficient.

#Get the final 10 characters from each number
#If there are fewer than 10, get them all
for x in selfPowers:
    sX = str(x)
    if len(sX) < 10:
        selfPowerSuffixes.append(sX)
    else:
        #if there are any leading zeroes, we still want to keep them.
        #so we won't yet cast back to an integer/long
        selfPowerSuffixes.append(sX[-10:])


sum = 0
for suffix in selfPowerSuffixes:
    #If the suffix has length less than 10 then we just use its length
    for c in range(1, min(len(suffix)+1,11)):
        sum += int(suffix[-c]) * myPow(10, c-1)

#We only need the last 10 digits of the sum
print(str(sum)[-10:])
