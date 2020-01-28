#~ Let d(n) be defined as the sum of proper divisors of n
#~ (numbers less than n which divide evenly into n).
#~ If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair
#~ and each of a and b are called amicable numbers.

#~ For example, the proper divisors of 220 are
#~ 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#~ Evaluate the sum of all the amicable numbers under 10000.

from primeFuncs import *

factorDict = {}
amicableNumbers = {}
for i in range(2, 10000):

	#set the factors up for this number
	try:
		if factorDict[i]: pass
		else: exit("ERROR")
	except:
		factorDict[i] = findFactors(i)
	firstSum = sum(factorDict[i])

	#print("sum of "+str(i)+"'s factors is "+str(firstSum))

	#get the factors for the sum of the first number's factors
	try:
		if factorDict[firstSum]: pass
		else: exit("ERROR")
	except:
		factorDict[firstSum] = findFactors(firstSum)
	secondSum = sum(factorDict[firstSum])

	#print("sum of "+str(firstSum)+"'s factors is "+str(sum(factorDict[firstSum])))

	#If the sums of each factors list are reciprocal, then they are amicable numbers.
	if (secondSum == i) and not(firstSum == i):
		print(str(i)+" and "+str(firstSum)+" are amicable numbers")
		amicableNumbers[i] = True
		amicableNumbers[firstSum] = True

sum = 0
for key in amicableNumbers:
	sum += key
print(amicableNumbers)
print(sum)
