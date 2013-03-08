#~ Let d(n) be defined as the sum of proper divisors of n
#~ (numbers less than n which divide evenly into n).
#~ If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair
#~ and each of a and b are called amicable numbers.

#~ For example, the proper divisors of 220 are 
#~ 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#~ Evaluate the sum of all the amicable numbers under 10000.

def sumFactors(n):
	x = (n/2)+1
	factorsList = []
	while (1):
		if (x == 0):
			break
		if ((n % x) == 0):
			factorsList.append(x)
		x -= 1
	sum = 0
	for i in range(len(factorsList)):
		sum += factorsList[i]
	return sum

def check_Prime(n):
	for i in range(n-1, 1, -1):
		if ((n%i) == 0):
			return False
	primeList.append(n)
	return True

amicableNum = 0
totalSum = 0

for i in range(1, 221):
	amicableNum = sumFactors(i)
	if (sumFactors(i) == sumFactors(amicableNum)):
		
		print i
		print amicableNum
		print sumFactors(i)
		print sumFactors(amicableNum)
		print
		
	
		
	
