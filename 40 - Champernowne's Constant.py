"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

<<<<<<< HEAD
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def getDigitsOfNaturalSequence(_targets):
    targetValues = []
    n = 0  #n increments one by one to know which digits to add onto the fraction
    t = 0   #t increments throughout the targets list when we've found one of the targets

    #keeps track of how long the fraction is so that we know when to save a value
    fractionLength = 0

    while n < _targets[-1] and t < len(_targets):
        currLength = len(str(n))
        n+=1

        #print(n, _targets[t], fractionLength, currLength)

        #if adding this next string of n onto the total fraction length would exceed one of the targets,
            #but it doesn't currently, then the target digit appears in n.
        while (t < len(_targets)) and (fractionLength + currLength >= _targets[t]) and (fractionLength <= _targets[t]):

            difference = fractionLength + currLength - _targets[t]

            #print("extra", n, _targets[t], difference, fractionLength, currLength)

            targetValues.append(int( str(n)[difference] ))

            t += 1      #we move on to the next target

            #Adjust if we are passing from one length of number to another

        #adjust the fraction's total length to reflect the addition of n
        fractionLength += currLength

    assert(t == len(_targets))

    return targetValues

#Tests the digits function on a specified target list. Digits must be in ascending order
def testDigitsFunction(_targets):
    digits = getDigitsOfNaturalSequence(sorted(_targets))
    product = 1
    for v in digits:
        product *= v
    print(digits, product)

#Test for the euler problem 40
#testDigitsFunction([1, 10, 100, 1000, 10000, 100000, 1000000])


#For some reason, it gets the 11th digit as 1 instead of 0 like it should.
#Issue doesn't seem to happen in the [99,101] range where it flips to length 3.
testDigitsFunction([9,10,11,12])
