#~ The prime factors of 13195 are 5, 7, 13 and 29.
#~ What is the largest prime factor of the number 600851475143 ?

from primeFuncs import *



def uniquePrimeFactorization(n):
	primeFactors = []
	i = 2
	while i < (n/2)+1:
		if n % i == 0:
			if check_Prime(i):
				print(str(i)+" is a prime factor, resetting target to "+str(n/i))
				primeFactors.append(i)

				#reset the target and loop counter
				n = n/i
				i = 2
		i+=1
	#adjust for the final prime factor, for which no prime factors were found
	primeFactors.append(n)
	return(primeFactors)

target = 600851475143

print(uniquePrimeFactorization(target))
