"""
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

from pandigitalFuncs import countListFromList


#We need to be able to create digits
#01, 04, 09, 16, 25, 36, 49, 64, and 81.
numAssociations = dict()
numAssociations[0] = [1,4,6]    #9 is also a possibility
numAssociations[1] = [0,6,8]    #9 is also a possibility
numAssociations[2] = [5]
numAssociations[3] = [6]        #9 is also a possibility
numAssociations[4] = [0,6]      #9 is also a possibility
numAssociations[5] = [2]
numAssociations[6] = [1,3,4]
numAssociations[7] = []         #7 doesn't appear in any squares <= 100
numAssociations[8] = [1]
numAssociations[9] = [0,4]

#The "extended set" for the pair of cubes must have numbers at least as large for each index as this list
minimalCubeRequirement = [1,1,1,1,1,1,1,0,1,1]

def cubeListGreatEnough(_cubeList, _requirementList=minimalCubeRequirement):
    requirements = True
    for i in range(10):
        if _requirementList[i] > _cubeList[i]:
            requirements = False
    return(requirements)


cubeCombinations = 0

for a in range(0,10):
    cubeOne = [a]
    cubeTwo = numAssociations[a]

    #print(cubeOne, cubeTwo)
    for b in range(0,10):
        if not(b in cubeOne):
            #print("  ", cubeOne+[b], list(set(cubeTwo + numAssociations[b])))

            for c in range(0,10):
                if not(c in cubeOne+[b]):
                    #print("    ", cubeOne+[b,c], list(set(cubeTwo + numAssociations[b] + numAssociations[c])))

                    #There are no solutions involving only 3 numbers on the first die

                    for d in range(0,10):
                        if not(d in cubeOne+[b,c]):

                            #prevent any combination which requires too many numbers on the other side
                            if len(list(set(cubeTwo + numAssociations[b] + numAssociations[c] + numAssociations[d]))) <= 6:
                                splitList = [cubeOne+[b,c,d], list(set(cubeTwo + numAssociations[b] + numAssociations[c] + numAssociations[d]))]
                                x = countListFromList(splitList[0] + splitList[1], 9, False)
                                if cubeListGreatEnough(x):
                                    print("Solution!", splitList[0], splitList[1])

    print()

    #x = countListFromList(cubeOne+cubeTwo, 9, False)
    #print(x)


#Heuristics:
#   7 is only usable in a combination which already represents everything with 5 of them
#   Every time we have 6 in a list, we should also consider it to have 9 in the list    (late adjustment)
