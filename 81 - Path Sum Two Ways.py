import os

class Node:
    def __init__(self, _val):
        self.val = _val
        self.right = 0
        self.down = 0


#get the number path information
numbers = []
#with open(os.getcwd()+'\\Euler\\18.txt') as f:
with open('euler\\81.txt') as f:
    data = f.readlines()
    for line in data:
        numbers.append([int(x) for x in line.split(',')])

#convert the 2d list of numbers into a 2d list of Node objects
numberObjects = []
numRows = len(numbers)
i = 0
while i < numRows:
    j = 0
    objectRow = []
    while j < len(numbers[i]):
        objectRow.append(Node(numbers[i][j]))
        j += 1

    numberObjects.append(objectRow)
    i +=1


#initialize the final element, which has 0 available moves remaining
numberObjects[-1][-1].right = numberObjects[-1][-1].val
numberObjects[-1][-1].down = numberObjects[-1][-1].val

#preload the right-moves for the final row (since going right is the only option)
#loop iterates from rightmost column to leftmost
for i in range(len(numberObjects[0])-2, -1, -1):
    numberObjects[-1][i].right = numberObjects[-1][i].val + numberObjects[-1][i+1].right

    #since there are no down-moves allowed at this node, we fix the "down value" to be the same as the right value.
    numberObjects[-1][i].down = numberObjects[-1][i].right

#preload the down-moves for the final column (since going down is the only option)
#loop iterates from bottom row to top
for i in range(len(numberObjects)-2, -1, -1):
    numberObjects[i][-1].down = numberObjects[i][-1].val + numberObjects[i+1][-1].down

    #since there are no right-moves allowed at this node, we fix the "right value" to be the same as the down value.
    numberObjects[i][-1].right = numberObjects[i][-1].down


#for each row, collapse the right/down values of the items around it
i = len(numberObjects)-2
while i >= 0:
    j = len(numberObjects[i])-2
    while j >= 0:
        numberObjects[i][j].down = numberObjects[i][j].val + min(numberObjects[i+1][j].right, numberObjects[i+1][j].down)
        numberObjects[i][j].right = numberObjects[i][j].val + min(numberObjects[i][j+1].right, numberObjects[i][j+1].down)

        #print("down and right of "+str(numberObjects[i][j].val)+" are "+str(numberObjects[i][j].down)+","+str(numberObjects[i][j].right))
        j -= 1

    i -= 1

print("The minimum path from %s has a sum of %s" % (numberObjects[0][0].val, min(numberObjects[0][0].down, numberObjects[0][0].right)))
