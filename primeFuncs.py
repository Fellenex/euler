import math

#This function was stripped directly from problem 7, where it was
#written to find the 10001st prime.
def check_Prime(n):
	n = abs(n)
	#print("Checking primality of "+str(n))
	i = n-1
	while (i > 1):
		if ((n%i) == 0):
			return False
		i -= 1
	return True

#Written for problem 58, when old check_Prime was far too inefficient
def checkPrimeEfficiently(_n):
	n = abs(_n)
	i = 2
	s = math.sqrt(n) + 1
	while (i < s):
		if ((n % i) == 0):
			return False
		i += 1
	return True

#Gets a list of factors for n
def findFactors(_n):
	if _n == 1 or _n == 2: return([1])
	i = (_n/2)+1
	factorsList = []
	while (i > 0):
		if ((_n % i) == 0):
			factorsList.append(i)
		i -= 1
	factorsList.reverse()
	return(factorsList)

#Returns a list of integers of the prime factors of _n
def uniquePrimeFactorization(_n):
	primeFactors = []
	i = 2
	while i < (_n/2)+1:
		if _n % i == 0:
			if check_Prime(i):
				#print(str(i)+" is a prime factor, resetting target to "+str(_n/i))
				primeFactors.append(i)

				#reset the target and loop counter
				_n = _n/i
				i = 2
		else:
			i += 1
	#adjust for the final prime factor, for which no prime factors were found
	primeFactors.append(int(_n))
	primeFactors.sort()
	return(primeFactors)

#Returns the greatest common divisor of two integers _a and _b
def gcd(_a,_b):
	while not(_a == _b):
		if _a > _b:
			_a -= _b
		else:
			_b -= _a
	return(_a)

#Returns Boolean indicating whether integers _a and _b are coprime
def coprime(_a,_b):
	return(gcd(_a,_b) == 1)
	

#this version of the sieve function utilizes two arrays, one with
#numbers, and one with True/False values (True indicating prime and
#False indicating non-prime). It assumes they are prime, then works
#to prove that numbers are not by removing all of the multiples of
#other numbers
def sieve_of_eratos_two(n):
	primeList = []
	numList = []

	p = 2
	carryOn = True
	for i in range(1, n+1):
		primeList.append(True)
		numList.append(i)

	#note, all values referenced in the primeList will be offset by -1 due to 0-based addressing
	while (carryOn):
		carryOn = False
		for i in range(2, ((n/2)+1)):
			if (p*i <= len(primeList)):
				primeList[(p*i)-1] = False
				carryOn = True
		for j in range(p+1, n):
			if (primeList[j-1] == True):
				p = j
				break

	return(primeList)


#More space-efficient version of eratosthenes' sieve
#(using dictionaries this time, instead of giant lists)
def sieve_of_eratos_three(n):
	p = 2
	carryOn = True
	primeDict = {}

	while (carryOn):
		carryOn = False
		for i in range(2, ((n/2)+1)):
			if (p*i) <= n+1:
				primeDict[(p*i)-1] = False
				carryOn = True
		for j in range(p+1, n):
			try:
				if primeDict[j-1] == False:
					pass
				else:
					p = j
					break
			except KeyError:
				p = j
				break

	return(primeDict)

def sieve_of_atkin_set(_n):
	primeDict = {}
	if _n > 2: primeDict[2]=True
	if _n > 3: primeDict[3]=True

	i = 1
	while (i*i < _n):
		j = 1
		while (j*j < _n):
			x = 4*(i*i) + (j*j)
			if (x <= _n and (x%12 == 1 or x%12 == 5)):
				try:
					#manual XOR since we don't initialize the list
					if primeDict[x] == True:
						primeDict[x] = False	#True XOR True is False
					else:
						primeDict[x] = True		#False XOR True is True
				except KeyError:
					#if it hasn't been indexed yet, then it means it's False
					#	(the default value which would've been set)
					#	so the XOR would resolve to True
					primeDict[x] = True

			x = 3*(i*i) + (j*j)
			if (x <= _n and x%12 == 7):
				try:
					if primeDict[x] == True:
						primeDict[x] = False
					else:
						primeDict[x] = True
				except KeyError:
					primeDict[x] = True

			x = 3*(i*i) - (j*j)
			if (i > j and x <= _n and x%12 == 11):
				try:
					if primeDict[x] == True:
						primeDict[x] = False
					else:
						primeDict[x] = True
				except KeyError:
					primeDict[x] = True
			j+=1
		i+=1

	r = 5
	while (r*r < _n):
		try:
			if primeDict[r]:
				for i in range(r*r, _n, r*r):
					primeDict[i] = False
		except KeyError:
			#we were only removing multiples of squares.
			#if it was never set, we don't need to reset it to false
			pass
		r+=1

	primeSet = set()
	for key in primeDict:
		if primeDict[key]:
			primeSet.add(key)

	return(primeSet)

#An actually efficient sieve algorithm, modified
#	to be more space-efficient with the use of dictionaries.
#Finds all primes below supplied integer n.
#Since we don't initialize the value of each integer,
#	there is some sketchy repeated try/except code to calculate the XOR.
#Factoring it out would mean passing the data structure around.
def sieve_of_atkin(_n):
	return(list(sieve_of_atkin_set(_n)))
