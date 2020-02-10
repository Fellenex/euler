
from primeFuncs import sieve_of_atkin, check_Prime

#sieveSize 20'000'000 only gets us to side length 4471 (~12.74% primality)
#sieveSize 30'000'000 only gets us to side length 5481 (~12.31% primality)
#sieveSize 50'000'000 only gets us to side length 7079 (~11.85% primality)
sieveSize = 50000000

primes = sieve_of_atkin(sieveSize)
primes.sort()
print(len(primes))

sideLength = 3
active = 1

denominator = 0
numerator = 0
primeRatio = 0

while primeRatio >= 0.10 or numerator == 0:
    for i in range(3):
        active += sideLength-1
        denominator += 1

        #Check to see if this number has been memoized as prime
        if active in primes:
            numerator += 1

        #If we haven't memoized this prime already, then check for it manually
        elif active > sieveSize:
            if check_Prime(active):
                print("Checking primes manually now")
                numerator += 1

        #active is not in primes, and is not larger than the sieve size, so it is composite
        else: pass

    #Bottom-right diagonal is always a square.
    #We increase the active number and denominator, but don't bother checking primality
    active += sideLength-1
    denominator += 1

    primeRatio = (numerator*1.0)/denominator
    if primeRatio < 0.13:
        print("At side-length "+str(sideLength)+" we have "+str(primeRatio)+"% primality")

    sideLength += 2

sideLength -= 2

print(sideLength)
