#Returns a list of the first _n pentagonal numbers
def generatePentagonals(_n):
    return([int(i*(3*i-1)/2) for i in range(1,_n+1)])


#Goes high up enough to find the first (and correct) solution
listSize = 3000
pents = generatePentagonals(listSize)

#Start them off at 10 since we know 1,5 have a smaller difference right away
minimumPair = (10,0)
minimumDiff = 10000000000000

for i in range(listSize):
    for j in range(i+1, listSize):
        diff = pents[j]-pents[i]
        #print(pents[i],pents[j],diff)

        if pents[i]+pents[j] in pents:
            if diff in pents:
                print(pents[i],pents[j]," a possible pair")
                if diff < minimumDiff:
                    minimumDiff = diff
                    minimumPair = (pents[i],pents[j])
                    print("New best is with ("+str(pents[i])+","+str(pents[j])+")")

print(minimumDiff)
print(minimumPair)
print(abs(minimumPair[0]-minimumPair[1]))
