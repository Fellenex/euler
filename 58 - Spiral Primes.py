
from primeFuncs import checkPrimeEfficiently
import time

targetRatio = 0.10

sideLength = 3
active = 1

denominator = 1
numerator = 0
primeRatio = 0

while primeRatio >= targetRatio or numerator == 0:
    for i in range(3):
        active += sideLength-1
        denominator += 1

        if checkPrimeEfficiently(active):
            numerator += 1


    #Bottom-right diagonal is always a square.
    #We increase the active number and denominator, but don't bother checking primality
    active += sideLength-1
    denominator += 1

    primeRatio = (numerator*1.0)/denominator
#    if primeRatio < 0.12:
#        print("At side-length "+str(sideLength)+" we have "+str(primeRatio)+"% primality ("+str(numerator)+"/"+str(denominator)+")")

    sideLength += 2

sideLength -= 2

print(sideLength)
