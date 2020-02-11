from numberSequences import *


#By testing with 100'000 for each value, we find that we only need to go up to (55385, 31977, 27693)
#rangeLimits = (100000,100000,100000)
rangeLimits = (55385, 31977, 27693)

triangles = generateTriangulars(rangeLimits[0])
pentagons = generatePentagonals(rangeLimits[1])
hexagons = generateHexagonals(rangeLimits[2])

for a in triangles:
    if a in pentagons and a in hexagons:
        print(str(a)+" is a triangular, pentagonal, and hexagonal number")
