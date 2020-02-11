"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
    there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

import math

def isValidRightTriangle(a,b,c):
    return (a*a + b*b == c*c)




rightTriangleSolutionsByPerimeter = []

#we won't append anything to the 0-index list,
#   and the 1001th index will be for perimeter 1000
for i in range(1001):
    rightTriangleSolutionsByPerimeter.append([])


for a in range(1,1001):
    #don't need to consider all values for b, since a<=b will cover all possibilities
    #e.g., if a,b,c is a solution, then b,a,c is a solution
    for b in range(a,1001):
        c = math.sqrt(a*a + b*b)

        #only consider solutions where c is an integer
        if int(c) == c:
            c = int(c)
            #perimeter must be less than 1000 to be a valid solution
            p = a + b + c
            if p <= 1000:
                rightTriangleSolutionsByPerimeter[p].append((a,b,c))

maxSolutionLength = 0
maxPerimeterSolution = None
for i in range(1,1001):
    if len(rightTriangleSolutionsByPerimeter[i]) > maxSolutionLength:
        maxSolutionLength = len(rightTriangleSolutionsByPerimeter[i])
        maxPerimeterSolution = i

print(maxSolutionLength)
print(maxPerimeterSolution)
