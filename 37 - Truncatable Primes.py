"""
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from primeFuncs import sieve_of_atkin_set


maxPrime = 1000000
primes = sieve_of_atkin_set(maxPrime)
truncatables = []

for p in primes:
    sP = str(p)
    doublyTruncatable = True

    #left truncations. e.g., 3797 --> {797, 97, 7}
    for j in range(1,len(sP)):
        if not(int(sP[j:]) in primes):
            doublyTruncatable = False

    #right truncations. e.g., 3797 --> {379, 37, 3}
    for j in range(1,len(sP)):
        if not(int(sP[:-j]) in primes):
            doublyTruncatable = False

    if doublyTruncatable:
        print(sP+" is doubly truncatable")
        truncatables.append(p)

truncatables.sort()

#Correct for the single-digit primes which don't count as truncatable.
for invalid in [2,3,5,7]:
    truncatables.remove(invalid)

print(truncatables)
print(sum(truncatables))
assert(len(truncatables) == 11)
