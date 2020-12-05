"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

max = 10000001
targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
numTargets = len(targets)

#where we'll store the digits we want to multiply. We skip over 1
targetValues = [1]

n = 1  #n increments one by one to know which digits to add onto the fraction
t = 1   #t increments throughout the targets list when we've found one of the targets

#keeps track of how long the fraction is so that we know when to save a value
fractionLength = 1

while n < max and t < numTargets:
    currLength = len(str(n))
    n += 1

    #if adding this next string of n onto the total fraction length would exceed one of the targets,
        #but it doesn't currently, then the target digit appears in n.
    if (fractionLength + currLength >= targets[t]) and (fractionLength <= targets[t]):

        difference = fractionLength + currLength - targets[t]
        targetValues.append(int(str(n)[difference]))

        t += 1      #we move on to the next target

    #adjust the fraction's total length to reflect the addition of n
    fractionLength += currLength

print(targetValues)
product = 1
for v in targetValues:
    product *= v
print(product)
