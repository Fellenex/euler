"""
P97
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×(2^7830457)+1.

Find the last ten digits of this prime number.
"""

precision = 10
precisionPower = 10 ** precision        #remove digits using modular arithmetic

def suffixingDigitsOfExponential(base, power, precision=3):
    rollingDigits = base
    for i in range(2, power+1):
        rollingDigits = (rollingDigits * base) % precisionPower

    print("The last %s digits of %s^%s are %s" % (precision, base, i, rollingDigits))
    return(rollingDigits)

k = 28433
power = 7830457
base = 2

n = suffixingDigitsOfExponential(base,power,precision)
n = ((k * n)+1) % precisionPower
print(n)
