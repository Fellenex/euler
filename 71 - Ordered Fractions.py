"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""

from primeFuncs import gcd

d = 10000

#We can reduce the overall range by only saving fractions that are less than 3/7
#We don't care about the ones that occur to the right, anyways.
maximalFraction = 3.0 / 7.0

#We can also heuristically lower-bound things
closestFraction = 3.0 / 8.0

#TODO:
#Once we've found i/j < 3/7, i/(j+1) << 3/7.
#e.g., no need to continue from 1/3 to 1/4 to ... 1/d
#   the first i/j we find is the largest for any j.

for i in range(1,d/2):
    for j in range((2*i)+1,d):
        activeFraction = i / (j * 1.0)
        if activeFraction < maximalFraction:
            if activeFraction > closestFraction:
                if gcd(i,j)==1:

                    #shrink the window of relevant fractions
                    closestFraction = activeFraction
                    #print("Adjusting to new min "+str(closestFraction))
            else:
                #activeFraction < closestFraction
                #Once we've found i/j < 3/7, i/(j+1) << 3/7.
                #e.g., no need to continue from 1/3 to 1/4 to ... 1/d
                #   the first i/j we find is the largest i/j for any j with fixed i.
                break

        else:
            pass
            #logic to do
            #   If i/j > 3/7, then also (i+1)/j > 3/7

print(closestFraction)

exit()

#minimalFraction = 3.0 / 7.0

#Create all possible fractions 3/8 < i/j < 3/7 where 1 <= i < j <= d
fractionDict = {}

#Since 3/7 < 1/2, we can consider only numerators that are at most d/2
for i in range(1,d/2):

    #Since 3/7 < 1/2, we can consider only denominators that are at least 2*i
    for j in range(2*i,d):
        activeFraction = i / (j * 1.0)
        if (activeFraction < maximalFraction) and (activeFraction > minimalFraction):

            #only save the fractions whose reduced form we've yet to find
            #since we're ordering (i,j) from smallest to largest, the first one we find will be reduced.
            if not(activeFraction in fractionDict):
                fractionDict[activeFraction] = (i,j)

print(fractionDict)

#Remove duplicate fractions, and create a sorted list out of the reduced fractions
reducedFractions = []
for f in sorted(fractionDict.keys()):
    reducedFractions.append(fractionDict[f])

print(reducedFractions)

#Since we only saved fractions smaller than 3/7,
#   the last fraction in the list will be "to the left" of 3/7 in the ordering.
print("The fraction to the left of 3/7 is "+str(reducedFractions[-1]))
