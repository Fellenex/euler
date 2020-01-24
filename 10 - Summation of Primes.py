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

#this function runs quite slowly for a sieve
#this is because of the "if (p*1) in numList" line.
#Time-differences show that the next sieve algorithm runs MUCH quicker
#There is also a lot of extra unnecessary added time due to the recounting numList every time
#it creates an array of all numbers from 2 to n, and
#then it checks that array for any multiples of numbers
#that have not been removed yet (which should be prime)
def sieve_of_eratos(n):
	p = 2
	count = 1
	removed = 0
	while (1):
		for i in range(2, n+1):
			if (p*i) in numList:
				numList.remove(p*i)
				removed +=1
		if removed == 0:
			break
		p = numList[count]
		count+=1
		removed = 0

#this version of the sieve function utilizes two arrays, one with
#numbers, and one with True/False values (True indicating prime and
#False indicating non-prime). It assumes they are prime, then works
#to prove that numbers are not by removing all of the multiples of
#other numbers

def sieve_of_eratos_two(n):
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

	primeSum = 0
	for key in primeDict:
		primeSum += key
	print(primeSum)


sum = 0
x = 2000000
numList = []
primeList = []

#This section of code compares the two Sieve functions. The second one runs slower with lower values
#but it will dramatically increase speed as the size increases.
while (1):
#	start = time.clock()
#	sieve_of_eratos(x)
#	finish = time.clock()
#	print ("Sieve of Eratosthenes with {0} took: \t {1} time".format(x, (finish-start)))

#	start = time.clock()
#	sieve_of_eratos_two(x)
#	finish = time.clock()
#	print ("Sieve of Eratosth Two with {0} took: \t {1} time".format(x, (finish-start)))

	#start = time.clock()
	#sieve_of_eratos_three(x)
	#finish = time.clock()
	#print ("Sieve of Eratosth Three with {0} took: \t {1} time".format(x, (finish-start)))

	start = time.clock()
	sieve_of_atkin(x)
	finish = time.clock()
	print ("Sieve of Atkin with {0} took: \t {1} time".format(x, (finish-start)))

	if x > 2000000:
		break

	x *= 2

#sieve_of_eratos_two(2000000)
#for i in range(len(numList)):
#	if primeList[i] == True:
#		sum += numList[i]
#print sum
