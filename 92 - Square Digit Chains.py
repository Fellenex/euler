"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""


squareDigitDict = dict()
for i in range(10):
    squareDigitDict[str(i)] = i*i

#For _n with digits n1 ... nx, gets (n1)*(n1) + ... + (nx) * (nx)
def getSumOfDigitsSquared(_n):
    _s = str(_n)
    squareSum = 0

    for c in _s:
        #using int(c)*int(c) takes a /lot/ longer, so we have a helper dict that stores them by string.
        squareSum += squareDigitDict[c]

    return(squareSum)



target = 10000000
eightyNineSet = set()
eightyNineArrival = 0

for i in range(1,target):

    #keep track of the i's in this chain.
    #if original i eventually leads to 89, then we'll keep track of all of the chain
    intermediaries = set()
    intermediaries.add(i)

    while not(i==1 or i==89):
        i = getSumOfDigitsSquared(i)

        if i in eightyNineSet:
            #we've already found that this one eventually arrives at 89 - just skip the rest
            i = 89

        else:
            #continue to keep track of i's, in case they eventually lead to 89
            intermediaries.add(i)

    if i == 89:
        eightyNineArrival += 1
        eightyNineSet.update(intermediaries)


print("There are "+str(eightyNineArrival)+" numbers below "+str(target)+" whose sum of digital squares leads to 89")
