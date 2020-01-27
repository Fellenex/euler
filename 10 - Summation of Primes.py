#~ The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#~ Find the sum of all the primes below two million.

import time

#was going to use this function, but it has sluggish time
#This function was stripped directly from problem 7, where it was
#written to find the 10001st prime.
def check_Prime(n):
	for i in range(n-1, 1, -1):
		if ((n%i) == 0):
			return False
	primeList.append(n)
	return True


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

#An actually efficient sieve algorithm, modified
#	to be more space-efficient with the use of dictionaries.
#Finds all primes below supplied integer n.
#Since we don't initialize the value of each integer,
#	there is some sketchy repeated try/except code to calculate the XOR.
#Factoring it out would mean passing the data structure around.
def sieve_of_atkin(n):
	primeDict = {}
	if n > 2: primeDict[2]=True
	if n > 3: primeDict[3]=True

	i = 1
	while (i*i < n):
		j = 1
		while (j*j < n):
			x = 4*(i*i) + (j*j)
			if (x <= n and (x%12 == 1 or x%12 == 5)):
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
			if (x <= n and x%12 == 7):
				try:
					if primeDict[x] == True:
						primeDict[x] = False
					else:
						primeDict[x] = True
				except KeyError:
					primeDict[x] = True

			x = 3*(i*i) - (j*j)
			if (i > j and x <= n and x%12 == 11):
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
	while (r*r < n):
		try:
			if primeDict[r]:
				for i in range(r*r, n, r*r):
					primeDict[i] = False
		except KeyError:
			#we were only removing multiples of squares.
			#if it was never set, we don't need to reset it to false
			pass
		r+=1

	primesList = []
	fakePrimes = []
	for key in primeDict:
		if primeDict[key]:
			primesList.append(key)

	return(primesList)



def compareSieves():
	x = 250
	while (x < 16001):
		start = time.clock()
		sieve_of_eratos_two(x)
		finish = time.clock()
		print ("Sieve of Eratosthenes with {0} took: \t {1} time".format(x, (finish-start)))

		start = time.clock()
		sieve_of_eratos_three(x)
		finish = time.clock()
		print ("Sieve of Eratosthenes with {0} took: \t {1} time".format(x, (finish-start)))

		start = time.clock()
		sieve_of_atkin(x)
		finish = time.clock()
		print ("Sieve of Eratosthenes with {0} took: \t {1} time".format(x, (finish-start)))

		x *= 2


maxValue = 2000000
primes = sieve_of_atkin(maxValue)
print(primes)
print("Found "+str(len(primes))+" below "+str(maxValue))
print("The sum of these primes is "+str(sum(primes)))
