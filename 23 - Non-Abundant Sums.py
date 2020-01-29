#~ A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
#~For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#~ A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#~ As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as
#~the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
#~than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
#~any further by analysis even though it is known that the greatest number that cannot be expressed as
#~the sum of two abundant numbers is less than this limit.

#~ Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from primeFuncs import findFactors


#returns -1 if a number is deficient (the sum of its divisors is less than n)
#returns 0 if a number is perfect (the sum of its divisors is exactly n)
#returns 1 if a number is abundant (the sum of its divisors is greater than n)
def numPerfection(n):
	factorSum = sum(findFactors(n))
	if (factorSum < n):
		return(-1)
	elif (factorSum == n):
		return(0)
	else:
		return(1)


abundantList = []
#since this is the lowest upper limit that is known, even though the real upper limit is less than this
for i in range(1, 28124):
	#find all the abundant numbers
	if (numPerfection(i) == 1):
		abundantList.append(i)


abundantListLength = len(abundantList)

#initialize a list of Falses to keep track of which numbers can be acquired through summing two abundant numbers
abundantSumPossible = [False]*((abundantList[-1]*2)+1)

#determine which the numbers which can be created from the sum of two abundant numbers
for j in range(abundantListLength):
	for k in range(j,abundantListLength):
		abundantSumPossible[abundantList[j] + abundantList[k]] = True



#Sum up all of the numbers < 28124 which cannot be created summing two abundant numbers
#	(recall every number >=28124 /can/ be made summing two abundant numbers)
nonAbundantSum = 0
for i in range(1,28124):
	if not(abundantSumPossible[i]):
		print(str(i)+" cannot be created summing two abundant numbers")
		nonAbundantSum += i

print(nonAbundantSum)
