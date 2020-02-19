"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10'000 x d100'000 x d1'000'000
"""

relevantIndices = [1,1]
relevantNumbers = [1,10]

activeNumber = 10
digitIndex = 11

#We need to go up to a digit index of 10**6
maxRange = 1000000

for i in range(2,7):
    currPow = 10**i

    #increment the active number and the digit indices up to the next power of 10
    for j in range(currPow - (10**(i-1))):
        activeNumber += 1
        digitIndex += i
        print(activeNumber, "["+str(digitIndex-i+1)+","+str(digitIndex)+"]")

        if digitIndex >= currPow and digitIndex-i-1 < currPow:

            print("Take "+str(activeNumber)+" at index "+str(currPow - digitIndex - 1))
            relevantIndices.append(int(str(activeNumber)[currPow-digitIndex-1]))
            relevantNumbers.append(activeNumber)
            #print(relevantIndices)
            print

        if digitIndex >= maxRange: break
    if digitIndex >= maxRange: break

print(relevantIndices)
print(relevantNumbers)

prod = 1
for n in relevantIndices:
    prod *= n
print(prod)
