
"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has
    exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from pandigitalFuncs import countList
from stringCycleFuncs import allStringPermutations
import math

cubes = []

for i in range(10000):
    cubes.append(int(math.pow(i,3)))

countLists = []
#TODO:
for i in range(10000):
    countLists.append(countList(cubes[i],9,False))

for i in range(10000):
    permAlsoCubeCount = 0
    for j in range(i,10000):
        if countLists[i] == countLists[j]:
            permAlsoCubeCount += 1

    if permAlsoCubeCount > 4:
        print(str(cubes[i])+" has "+str(permAlsoCubeCount)+" permutations which are also cube.")


exit()
#Method which creates all permutations for each cube (takes way too long)
for i in range(1000):
    cubeLength = len(str(cubes[i]))
    perms = allStringPermutations(str(cubes[i]),cubeLength-1)

    #start at 0 because cubes[i] will be in perms
    permAlsoCubeCount = 0
    for p in perms:
        #TODO: a better method to avoid the removal of leading-0s when casting to integer
        if (int(p) in cubes) and (len(str(int(p))) == cubeLength):
            #print(p+" is cube")
            permAlsoCubeCount += 1

    if permAlsoCubeCount > 1:
        print(str(cubes[i])+" has "+str(permAlsoCubeCount)+" permutations which are also cube.")
