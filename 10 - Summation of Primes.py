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
	
	
		
sum = 0
x = 250
numList = []
primeList = []

#This section of code compares the two Sieve functions. The second one runs slower with lower values
#but it will dramatically increase speed as the size increases.
#~ while (1):
	#~ start = time.clock()
	#~ sieve_of_eratos(x)
	#~ finish = time.clock()
	#~ print ("Sieve of Eratosthenes with {0} took: \t {1} time".format(x, (finish-start)))

	#~ start = time.clock()
	#~ sieve_of_eratos_two(x)
	#~ finish = time.clock()
	#~ print ("Sieve of Eratosth Two with {0} took: \t {1} time".format(x, (finish-start)))
	
	#~ x *= 2
	#~ if x > 16001:
		#~ break
sieve_of_eratos_two(2000000)
for i in range(len(numList)):
	if primeList[i] == True:
		sum += numList[i]
print sum