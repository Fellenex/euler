import os

class Node:
    def __init__(self, _val):
        self.val = _val
        self.left = 0
        self.right = 0


#get the number path information
numbers = []
#with open(os.getcwd()+'\\Euler\\18.txt') as f:
with open(os.getcwd()+'\\67.txt') as f:
    data = f.readlines()
    for line in data:
        numbers.append(map(int, line.rstrip('\n').split(' ')))



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

#reverse the list so that we're working bottom-up
numberObjects.reverse()

#initialize the final row (since there are no lower left/right paths available)
for obj in numberObjects[0]:
    obj.left = obj.val
    obj.right = obj.val


#for each row, collapse the left/right values of the items below it
i = 1
while i < len(numberObjects):
    j = 0
    while j < len(numberObjects[i]):
        numberObjects[i][j].left = numberObjects[i][j].val + max(numberObjects[i-1][j].left, numberObjects[i-1][j].right)
        numberObjects[i][j].right = numberObjects[i][j].val + max(numberObjects[i-1][j+1].left, numberObjects[i-1][j+1].right)

        print("left and right of "+str(numberObjects[i][j].val)+" are "+str(numberObjects[i][j].left)+","+str(numberObjects[i][j].right))
        j+=1

    print
    i+= 1

#Two possible max values from the (original) root node
print(numberObjects[-1][-1].left)
print(numberObjects[-1][-1].right)
