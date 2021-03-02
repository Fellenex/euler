"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×(2^7830457)+1.

Find the last ten digits of this prime number.
"""


k = 28433
power = 7830457
base = 2

precision = 10
precisionPower = 10 ** precision        #remove digits using modular arithmetic

rollingDigits = base
i = 2
while i <= power:
    rollingDigits = (rollingDigits * base) % precisionPower
    i +=1

print("The last %s digits of %s^%s are %s" % (precision, base, i, rollingDigits))

#multiply by the factor, and the added constant
rollingDigits = (rollingDigits * k) % precisionPower

rollingDigits = (rollingDigits + 1) % precisionPower

print("The last %s digits of %s*(%s^%s)+1 are %s" % (precision, k, base, power, rollingDigits))
