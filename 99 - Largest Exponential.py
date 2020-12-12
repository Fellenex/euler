from primeFuncs import gcd, coprime
from math import log

expTuples = []
with open('99.txt') as f:
    for line in f.readlines():

        #turns each line of the textfile into a 2-element tuple for exponent and base.
        expTuples.append([int(x) for x in line.rstrip('\n').split(',')])


#indices of the tuples
BASE_INDEX = 0
EXP_INDEX = 1

maxTuple = (expTuples[0][BASE_INDEX], expTuples[0][EXP_INDEX])
maxLineNumber = 1

for i in range(1, len(expTuples)):

    #Now we take the log of each number, taking expTuples[i] as a^b, and maxTuple as c^d.
    l1 = expTuples[i][EXP_INDEX]        #log_a(a^(b)) == b
    l2 = maxTuple[EXP_INDEX] * log(maxTuple[BASE_INDEX], expTuples[i][BASE_INDEX])      #log_a(c^(d)) == (d) * log_a(c)

    if l1 > l2:
        #if the ith tuple is greater than the greatest we've seen so far, then change the greatest we've seen.
        maxTuple = (expTuples[i][BASE_INDEX], expTuples[i][EXP_INDEX])
        maxLineNumber = i

print(maxLineNumber)
print(maxTuple)
