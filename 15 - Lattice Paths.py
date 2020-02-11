"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

import math

#Gets the number of paths in a grid of size m x n using only right/down movements
def latticePaths(m,n):
    if (m==1) and (n==1):
        return(pathDict[(1,1)])
    elif (m==1):
        return(pathDict[1,n])
    elif (n==1):
        return(pathDict[m,1])
    else:
        #number of paths by going in one direction for this move
        try:
            x = pathDict[(m-1, n)]
        except KeyError:
            #print("("+str(m-1)+","+str(n)+") is as of yet undefined")
            x = latticePaths(m-1, n)
            pathDict[(m-1,n)] = x

        #number of paths by going in the other direction for this move
        try:
            y = pathDict[(m,n-1)]
        except KeyError:
            #print("("+str(m)+","+str(n-1)+") is as of yet undefined")
            y = latticePaths(m,n-1)
            pathDict[(m,n-1)] = y

        return(x+y)


#Define pathDict globally so that we're not passing it recursively over and over
pathDict = {}
pathDict[(1,1)]=2
for i in range(2,21):
    pathDict[(i,1)]=(i+1)
    pathDict[(1,i)]=(i+1)
    pathDict[(i,i)] = latticePaths(i,i)
    print("There are "+str(latticePaths(i,i))+" paths in a grid of size "+str(i)+"x"+str(i))
