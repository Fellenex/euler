#~ The prime factors of 13195 are 5, 7, 13 and 29.
#~ What is the largest prime factor of the number 600851475143 ?

import math

primesDictionary = dict()
primesDictionary[1]=False

def isPrime(_n):
	#If the number has already been memoized, then just return the value.
	if _n in primesDictionary:
		primeness = primesDictionary[_n]

	#Otherwise, determine whether or not it's prime.
	else:
		primeness = True
		for i in range(int(math.sqrt(_n)), 1, -1):
			if ((_n%i) == 0):
				primeness = False

		#Memoize it so that we don't do this work again.
		primesDictionary[_n] = primeness

	return primeness

def findFactors(_n):
	factors = []
	x = (_n/2)+1
	while x > 0:
		if ((_n % x) == 0):
			factors.append(x)
		x -= 1

	return factors

def main():
	n = 600851475143
	#n = 13195

	factorsList = findFactors(n)
	primeFactorsList = [p for p in factorsList if isPrime(p)]
	primeFactorsList.reverse()

	print primeFactorsList

main()
