"""
Euler discovered the remarkable quadratic formula:
  n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n=40, 402+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41, 412+41+41 is clearly divisible by 41.

The incredible formula n2-79n+1601
was discovered, which produces 80 primes for the consecutive values 0<=n<=79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
    n2+an+b,
    where |a|<1000 and |b| <= 1000
    where |n|
      is the modulus/absolute value of n
      e.g. |11|=11 and |-4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from primeFuncs import check_Prime


#Returns the value x such that n^2 + _an + _b is prime for all 0 <= n <= x,
#
def quadraticPrimeSequenceLength(_a,_b):
    n = 0
    while check_Prime(n*n + _a*n + _b):
        n+=1

    #Remove one for the first value which is not prime
    n -=1
    return(n)


print(quadraticPrimeSequenceLength(1,41))
print(quadraticPrimeSequenceLength(-79,1601))
print


longestSequence = 0
maxValues = (0,0)
possiblePrimes = []
#-1000 < a < 1000 and -1000 <= b <= 10000,
#   but neither -1000 or 1000 are prime, so we can
#   just use -1000 < b < 1000 as the range.
for x in range(-999, 1000):
    if check_Prime(x):
        possiblePrimes.append(x)

numPrimes = len(possiblePrimes)

#For any pair of primes in our list (including either direction, since a and b are not symmetric)
#   we check to see how many consecutive integers are prime, given n^2 + i*n + j
for i in range(numPrimes):
    for j in range(numPrimes):
        currSeqLength = quadraticPrimeSequenceLength(possiblePrimes[i],possiblePrimes[j])
        if currSeqLength > longestSequence:
            longestSequence = currSeqLength
            maxValues = (possiblePrimes[i], possiblePrimes[j])
            print("New longest sequence is "+str(currSeqLength)+", coming from ("+str(possiblePrimes[i])+","+str(possiblePrimes[j])+")")

print(maxValues[0] * maxValues[1])
