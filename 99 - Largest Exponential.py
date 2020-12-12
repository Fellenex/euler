from primeFuncs import gcd, coprime
from math import log

class ExpTuple:
    def __init__(self, base, exp):
        self.base = int(base)
        self.exp = int(exp)

expTuples = []
with open('99.txt') as f:
    for line in f.readlines():

        #turns each line of the textfile into a 2-element tuple for exponent and base.
        splitLine = line.rstrip('\n').split(',')
        expTuples.append(ExpTuple(splitLine[0], splitLine[1]))


maxLineNumber = 1       #the project euler problem wants the line number of the maximal expression.
#Initialize the maximum expression we've seen thus far.
maxTuple = ExpTuple(expTuples[0].base, expTuples[0].exp)

for i in range(1, len(expTuples)):
    #Now we take the log (base a) of each number, taking expTuples[i] as a^b, and maxTuple as c^d.
    l1 = expTuples[i].exp        #log_a(a^(b)) == b
    l2 = maxTuple.exp * log(maxTuple.base, expTuples[i].base)      #log_a(c^(d)) == (d) * log_a(c)

    if l1 > l2:
        #if the ith tuple is greater than the greatest we've seen so far, then change the greatest we've seen.
        maxTuple = expTuples[i]
        maxLineNumber = i

#We add one to the variable keeping track of the greatest expression's line number, since line count starts at 1.
maxLineNumber += 1

print("%s^%s is the maximal expression, appearing on line %s" % (maxTuple.base, maxTuple.exp, maxLineNumber))
