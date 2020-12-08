from primeFuncs import sieve_of_atkin
import matplotlib.pyplot as plt
import numpy as np


def phiFunction(_p1, _p2):
    smol = min(_p1, _p2)
    chomb = max(_p1, _p2)

    factor = (chomb // smol) + 1
    #print("%s*%s = %s is the first composite involving %s larger than %s, using factor %s" % (factor, smol, factor*smol, smol, chomb, factor))

    return(factor)



#why does 523's plot point scoop all the way backwards to the y origin
#primes = sieve_of_atkin(100000)
primes = sorted(sieve_of_atkin(5000))
#print(primes)


#plt.ylabel('Smallest composite involving smaller prime that is larger than larger prime')
#plt.xlabel('Larger primes')

#pairs = np.array([(primes[i], primes[j]) for i in range(len(primes)) for j in range(i)])

#print(primes)

dist = []
p =[]
for i in range(1,len(primes)):
    #for j in range(0,i):
        #fac = phiFunction(primes[j],primes[i])
    dist.append((2 * primes[i-1] - primes[i])/(2 * primes[i-1])
        #p.append(primes[i])



#print(dist)

#phiValues = [(((phiFunction(primes[i], primes[-1]) * primes[i]) - primes[-1]) / primes[-1]) for i in range(len(primes))]
plt.hist(dist)
#plt.plot(p,dist)
plt.show()


#phiValues = [phiFunction(primes[i],primes[j]) for i in range(len(primes)) for j in range(i)]
#print(phiValues)

exit()

plt.plot(phiValues)
plt.show()

exit()

smallPrimes = []
largePrimes = []
for p in pairs:
    largePrimes.append(p[0])
    smallPrimes.append(p[1])

#plt.plot(largePrimes, smallPrimes, label='pairs')




#plt.show()
#exit()



for pair in pairs:
    print(pair)



for x in range(len(primes)):
    for y in range(x):
        #print(primes[x],primes[y])
        phiFunction(primes[x],primes[y])


#plt.show()
