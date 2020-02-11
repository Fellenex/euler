import os

numberStrings = []
with open(os.getcwd()+'\\Euler\\13.txt') as f:
    for line in f.readlines():
        numberStrings.append(line.rstrip('\n'))


print(numberStrings)

numCount = len(numberStrings)
numLength = len(numberStrings[0])
colSums = []

#Add all the columns individually
j = -1
while -1*j < numLength+1:
    i = 0
    colSum = 0
    while i < numCount:
        colSum += int(numberStrings[i][j])
        i += 1

    #create a padding of 0s to adjust for each column's position in the sum
    paddingString = "0"*((j+1)*-1)
    colSums.append(int(str(colSum)+paddingString))

    print
    j -= 1

print(colSums)
print(sum(colSums))
