#~ The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#~ Find the sum of all the primes below two million.

import time
from primeFuncs import *



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
