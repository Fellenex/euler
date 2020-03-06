"""
Numerals must be arranged in descending order of size.
M, C, and X cannot be equalled or exceeded by smaller denominations.
D, L, and V can each only appear once.
"""

import os
from romanFuncs import *

with open(os.getcwd()+'\\89.txt') as f:
    romanNumerals = [ell.rstrip('\n') for ell in f.readlines()]
print(romanNumerals)

savedCharacters = 0
for r in romanNumerals:
    i = romanToInteger(r)
    ir = integerToRoman(i)
    savedCharacters += len(r) - len(integerToRoman(romanToInteger(r)))

print(savedCharacters)
