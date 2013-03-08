#~ The prime factors of 13195 are 5, 7, 13 and 29.
#~ What is the largest prime factor of the number 600851475143 ?

def check_Prime(n):
	for i in range(n-1, 1, -1):
		if ((n%i) == 0):
			return False
	primeList.append(n)
	return True

def find_Factors(n):
	x = (n/2)+1
	while (1):
		if (x == 0):
			break
		if ((n % x) == 0):
			factorsList.append(x)
		x -= 1


#This program works for smaller values, but it has not
#shown to work for the value 600851475143.
#This is because of the iterative nature of my algorithm
primeList = []
factorsList = []
primeFactorsList = []

find_Factors(83950)
largest = 0
for i in range (len(factorsList)):
	if check_Prime(factorsList[i]):
		primeFactorsList.append(factorsList[i])

primeFactorsList.reverse()
print primeFactorsList
	
