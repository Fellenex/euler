from primeFuncs import coprime, sieve_of_atkin


#TODO: Already for 10'000 this takes too long
target = 1001
maximumTotient = 0
maximumTotientCauser = 0

primes = sorted(sieve_of_atkin(target))

#Lehmer's conjecture: "If p is prime, then phi(p) = p-1"
#Resulting assumption: the number with the highest p/p-1 won't be a prime



for i in range(2,target):
    if not(i in primes):
        #all numbers are relatively prime to 1
        t = 1

        for j in range(2,i):
            if coprime(i,j):
                t += 1

        if i / (t*1.0) > maximumTotient:
            maximumTotient = i / (t*1.0)
            maximumTotientCauser = i

print("The maximum totient for n <= "+str(target)+" is "+str(maximumTotient)+", caused by "+str(maximumTotientCauser))
