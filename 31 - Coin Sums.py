"""
In the United Kingdom the currency is made up of pound (&) and pence (p). There are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, &1 (100p), and &2 (200p).

It is possible to make &2 in the following way:

    1x&1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can &2 be made using any number of coins?
"""

#There are ways which use only one kind of coin
#...
#There are ways which use 6 kinds of coins (100+50+20+10+5+2+1 = 188)


def waysWithCoins(_target, _solutionList=[]):
    if _target == 1:
        return([_solutionList+[1]])

    elif _target == 0:
        return([_solutionList])

    else:
        #If we've already memoized, then just send that value back
        if memoizedWays[_target]:
            print("We've already found "+str(_target))
            print("going to add "+str(memoizedWays[_target])+" to "+str(_solutionList))
            return(memoizedWays[_target])

        else:
            currSols = []
            if _target >= 200:
                for x in coinValues:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            elif _target >= 100:
                for x in coinValues[:7]:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            elif _target >= 50:
                for x in coinValues[:6]:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            elif _target >= 20:
                for x in coinValues[:5]:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            elif _target >= 10:
                for x in coinValues[:4]:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            elif _target >= 5:
                for x in coinValues[:3]:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            elif _target >= 2:
                for x in coinValues[:2]:
                    currSols += waysWithCoins(_target - x, _solutionList+[x])

            else:
                exit("ERROR")

        print("c"+str(currSols))
        return(currSols)


coinValues = [1,2,5,10,20,50,100,200]
coinIndexMap = {1:0, 2:1, 5:2, 10:3, 20:4, 50:5, 100:6, 200:7}
numCoins = len(coinValues)

#List for memoizing things (nuts to you, MemoryError!)
memoizedWays = [None]*200

memoizedWays[2]=[[1,1],[2]]
print(waysWithCoins(5))

exit()

for x in range(1,6):
    print("Starting "+str(x))
    wayLists = waysWithCoins(x)
    memoizedWays[x] = []

    #Turn the lists into dictionaries so that we can remove duplicates (whose ordering is different)
    wayDicts = []
    for way in wayLists:
        #print("w"+str(way))
        wd = {1:0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0}
        for coin in way:
            wd[coin] += 1

        #Don't add this dictionary in if there is already one with this signature (i.e., count for each coin)
        if not(wd in wayDicts):
            currentDictWays = []
            #print("wd"+str(wd))
            for key in wd:
                if not(wd[key] == 0):
                    currentDictWays += [key]*wd[key]
            #print("cd"+str(currentDictWays))
            memoizedWays[x].append(currentDictWays)

for x in range(10):
    print("Ways to split up "+str(x)+": "+str(memoizedWays[x]))
