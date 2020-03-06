"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

import os

with open(os.getcwd()+'\\79.txt') as f:
    codes = [ell.rstrip('\n') for ell in f.readlines()]

#Create a dictionary of sets so each number can refer to the numbers that must come before it
precededByDict = dict()
for i in range(10):
    precededByDict[str(i)] = set()

#Determine which values must come before each other value
for code in codes:
    precededByDict[code[2]].add(code[0])
    precededByDict[code[2]].add(code[1])
    precededByDict[code[1]].add(code[0])

for d in precededByDict:
    if len(precededByDict[d]) > 0:
        print(d, precededByDict[d])

#print(sorted(precededByDict.values()))

#Found solution:
    #73162890
#The code itself was derived from inspection.
