"""
Problem:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
  21 22 23 24 25
  20  7  8  9 10
  19  6  1  2 11
  18  5  4  3 12
  17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


Proof:
Diagonals:
  1
  3, 5, 7, 9
  13, 17, 21, 25
  31, 37, 43, 49

  First ring has diagonals (3,5,7,9)
    Spanning 2-9, the first ring contains 8 elements.
    The first diagonal is the second element in order, and every diagonal after that is 2 elements away.

  Second ring has diagonals (13,17,21,25)
    Spanning 10-25, the second ring contains 16 elements.
    The first diagonal is the fourth element in order, and every diagonal after that is 4 elements away.

  Third ring has diagonals (31,37,43,49)
    Spanning 26-49, the third ring contains 24 elements.
    The first diagonal is the sixth element in order, and every diagonal after that is 6 elements away.

  Let R be ring x
    Then R has 8x elements, spanning from 1+(2x-1)^2 to (2x+1)^2
    The first element is the last diagonal of the previous ring, plus one.
    The first diagonal is the 2x'th element, and every diagonal after that is 2x elements away.

In a 1x1 spiral, there is 1 element, 0 rings, 1 diagonal, and the last diagonal is 1.
In a 3x3 spiral, there are 9 elements, 1 rings, 5 diagonals, and the last diagonal is 9.
In a 5x5 spiral, there are 25 elements, 2 rings, 9 diagonals, and the last diagonal is 25.
In a 7x7 spiral, there are 49 elements, 3 rings, 13 diagonals, and the last diagonal is 49.
In an LxL spiral, there are L*L elements, floor(L/2) rings, 1 + floor(L/2)*4 diagonals, and the last diagonal is L*L.

In a 1001x1001 spiral:
  There are 1002001 elements, and 1002001 is the last element and diagonal.
  There are floor(1001/2) = 500 rings.

  Then the outermost ring has 4000 elements, spanning from 998002 to 1002001.
  First diagonal is at 1002001, and the next three are 1002001-(1000d), where d=1,2,3.

  So then from i=[500,2]:
    First diagonal is at (2i+1)^2
    Next diagonals are at (2i+1)^2 - (2i)*d, for d=1,2,3

    So then the sum of all of the diagonals in ring i is
    = 4((2i+1)^2) - 12i
    = 4((2i+1)^2 - 3i)

"""

import math

numRings = 500
mySum=1
for i in range(numRings,0,-1):
    maxValue = math.pow(2*i+1,2)
    mySum += 4*(maxValue - 3*i)

print mySum
#669171001
