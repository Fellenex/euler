#~ 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#~ What is the sum of the digits of the number 2^(1000)?

import math

def sumOfDigits(n):
	stringRep = str(n)
	sum = 0
	for i in range(len(stringRep)):
		sum += int(stringRep[i])
	return sum

num = 2
for i in range(1, 1000):
	num *= 2
print sumOfDigits(num)