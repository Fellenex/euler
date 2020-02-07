"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from primeFuncs import sieve_of_atkin

upperBound = 1000000

primes = sieve_of_atkin(upperBound)
primes.sort()

#since 21 consecutive primes can sum to 953, there must be
#   a sequence of 22 (or more) primes that can sum to a prime below 1'000'000
minWindowSize = 3

#Max window size is X, where the sum of the first X consecutive primes is below 1'000'000
s = 0
i = 0
while True:
    s += primes[i]
    i += 1
    if s >= upperBound:
        i -= 1
        s -= primes[i]
        break
maxWindowSize = i

print("Max possible window size is "+str(maxWindowSize)+" yielding a sum of "+str(sum(primes[0:maxWindowSize])))


#Start with maximum window size and work down.
#The first solution we find has the longest sequence adding up to a prime
for w in range(maxWindowSize, minWindowSize-1, -1):
    i = 0
    #recalculate the sum every time because it will be changing based on the value of i
    while sum(primes[i:i+w]) < upperBound:
        if sum(primes[i:i+w]) in primes:
            print("Found that "+str(sum(primes[i:i+w]))+" can be created using "+str(w)+" consecutive primes")
            exit()
        i += 1
