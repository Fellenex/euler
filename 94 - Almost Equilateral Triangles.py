import math
import time

"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area.
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""





#Area of a triangle with side lengths (x, x, x-1)
def heronFormulaThirdSideSmaller(x):
    return (1.0/4) * math.sqrt( ((3*x)-1)*(x-1)*(x-1)*(x+1) )

#Area of a triangle with side lengths (x, x, x+1)
def heronFormulaThirdSideLarger(x):
    return (1.0/4) * math.sqrt( ((3*x)+1)*(x+1)*(x+1)*(x-1) )


def isInteger(_n):
    return int(_n) == _n


def isoscelesArea(_a,_b):
    return (1.0/2) * _b * math.sqrt((_a*_a) - (_b*_b/4.0))



def isoAreaSmaller(_x):
    return (1.0 / 4) * (_x-1) * math.sqrt(3*_x*_x + 2*_x - 1)

def isoAreaBigger(_x):
    return (1.0 / 4) * (_x+1) * math.sqrt(3*_x*_x - 2*_x - 1)


upperBound = 1000000000
#upperBound = 10000000
maxSideLength = int(upperBound / 3.0)


"""
perimeterSums = 0
periOne = []
sOne = time.time()

for x in range(2, maxSideLength):
    if isInteger(heronFormulaThirdSideLarger(x)):
        t = math.sqrt(3*x*x - 2*x - 1)
        periOne.append((x,t))
        perimeterSums += (3*x)+1

    if isInteger(heronFormulaThirdSideSmaller(x)):
        t = math.sqrt(3*x*x + 2*x - 1)
        periOne.append((x,t))
        perimeterSums += (3*x)-1
fOne = time.time()

print(periOne)
print(perimeterSums)
"""
"""
perimeterSums = 0

sOne = time.time()
possibleLargerIsoLengths = []
possibleSmallerIsoLengths = []
for x in range(2, maxSideLength):
    if isInteger(math.sqrt(3*x*x - 2*x - 1)):
        possibleLargerIsoLengths.append(x)

    if isInteger(math.sqrt(3*x*x + 2*x - 1)):
        possibleSmallerIsoLengths.append(x)

#print("Large: ", possibleLargerIsoLengths)
#print("Small: ", possibleSmallerIsoLengths)

perimeterSums += sum((3*x) + 1 for x in possibleLargerIsoLengths)
perimeterSums += sum((3*x) - 1 for x in possibleSmallerIsoLengths)

fOne = time.time()
print(perimeterSums)
"""


#For triangle (5, 5, 6), we get that (x+1)/4 = 1.5, even though the area of (5,5,6) is 12.
#   Implication: The fractional part at the beginning does not need to be an integer.

#For triangle (302828, 302828, 302829), python evaluates the area as an integer - it is actually 39'709'429'597.0000028....
#So then we need a better way to evaluate whether the area is an integer.

#Assumption: No (x-1)/4 or (x+1)/4 is able to multiply by a repeating-digit fraction to create an integer.
#   Implication: The root part must be an integer
"""
perimeterSums = 0

foundInts = []
sTwo = time.time()
for x in range(2, maxSideLength):
    if isInteger(math.sqrt(3*x*x - 2*x - 1)):
        foundInts.append(x)
        perimeterSums += 3*x + 1

    if isInteger(math.sqrt(3*x*x + 2*x - 1)):
        foundInts.append(x)
        perimeterSums += 3*x - 1

fTwo = time.time()
print(perimeterSums)
print(foundInts)
"""


#most recent
"""
upperBound = 1000

perimeterSums = 0

sThree = time.time()

validLarger = [x for x in range(2, maxSideLength+1) if ( (x+1)/(4.0) * (math.sqrt(3*x*x - 2*x - 1)) ) % 1 == 0]
validSmaller = [x for x in range(2, maxSideLength+1) if ( (x-1)/(4.0) * (math.sqrt(3*x*x + 2*x - 1)) ) % 1 == 0]

#validLarger = [x for x in range(2, maxSideLength+1) if ( (math.sqrt(3*x*x - 2*x - 1))) % 1 == 0]
#validSmaller = [x for x in range(2, maxSideLength+1) if ( (math.sqrt(3*x*x + 2*x - 1))) % 1 == 0]
print(sum([3*x + 1 for x in validLarger]) + sum([3*x - 1 for x in validSmaller]))

print(sorted(validLarger + validSmaller)[:15])
fThree = time.time()
"""



"""From OEIS 120893: "For n>1, hypotenuse of primitive Pythagorean triangles having an angle nearing pi/3 for larger values of sides."""
def oeisSequence(_n):
    if not(_n in generatedSideLengths):
        generatedSideLengths[_n] = 3*oeisSequence(_n-1) + 3*oeisSequence(_n-2) - oeisSequence(_n-3)

    return generatedSideLengths[_n]


sFour = time.time()

generatedSideLengths = {0:1, 1:1, 2:5}
sumOfPerimeters = 0
i = 2       #the first triangle (5,5,6) uses index 2 of the sequence, and it increments from there
activeValue = oeisSequence(i)

print([oeisSequence(x) for x in range(0,16)])


while activeValue <= maxSideLength:

    #a triangle of the form (x, x, x+1)
    if (isoAreaBigger(activeValue) % 1) == 0:
        print("larger "+str(activeValue)+", adding "+str(activeValue * 3 + 1))
        sumOfPerimeters += (activeValue * 3) + 1

    #a triangle of the form (x, x, x-1)
    if (isoAreaSmaller(activeValue) % 1) == 0:
        print("smaller "+str(activeValue)+" adding "+str(activeValue * 3 - 1))
        sumOfPerimeters += (activeValue * 3) - 1


    print(sumOfPerimeters)
    i += 1
    activeValue = oeisSequence(i)



print(sumOfPerimeters)
fFour = time.time()

"""
sThree = time.time()
validLarger = [x for x in range(2, maxSideLength) if isInteger(math.sqrt(3*x*x - 2*x - 1))]
validSmaller = [x for x in range(2, maxSideLength) if isInteger(math.sqrt(3*x*x + 2*x - 1))]

print(sorted(validLarger + validSmaller))
print(sum([3*x + 1 for x in validLarger]) + sum([3*x - 1 for x in validSmaller]))

fThree = time.time()
"""


#print(fOne - sOne)
#print(fTwo - sTwo)
#print(fThree - sThree)
print(fFour - sFour)
