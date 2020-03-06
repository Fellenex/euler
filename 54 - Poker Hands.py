import os

class Card:
    def __init__(self, _val, _suit):
        self.val = _val
        self.suit = _suit

    def toString(self):
        return("The "+str(self.val)+" of "+self.prettySuit())

    def prettySuit(self):
        if self.suit == "C":
            return("Clubs")
        elif self.suit == "D":
            return("Diamonds")
        elif self.suit == "H":
            return("Hearts")
        elif self.suit == "S":
            return("Spades")

class Hand:
    def __init__(self, _cards):
        self.cards = _cards

        #Runs alphabetically: [C,D,H,S]
        self.suitCount = [0,0,0,0]
        for c in self.cards:
            if c.suit == "C":
                self.suitCount[0] += 1
            elif c.suit == "D":
                self.suitCount[1] += 1
            elif c.suit == "H":
                self.suitCount[2] += 1
            elif c.suit == "S":
                self.suitCount[3] += 1

        #Based off of pandigitalFuncs;countList()
        #But we need to count 10,J,Q,K as indices in the list, so it's not quite directly applicable
        self.rankCount = [0]*13
        for c in self.cards:
            if c.val == "A":
                self.rankCount[12] += 1
            elif c.val == "K":
                self.rankCount[11] += 1
            elif c.val == "Q":
                self.rankCount[10] += 1
            elif c.val == "J":
                self.rankCount[9] += 1
            elif c.val == "T":
                self.rankCount[8] += 1
            else:
                #offset the indices by 2 because our 0th index relates to element 2
                self.rankCount[int(c.val)-2] += 1

    def toString(self):
        return([s.toString() for s in self.cards])


    #There are 10 types of hands ranging from high card (1) to royal flush (10)
    #This function returns the rank value of the hand
    def ranking(self):
        rank=0

        #checking for straight consecutiveness
        straight = False
        for i in range(8):
            if self.rankCount[i:i+5] == [1,1,1,1,1]:
                straight = True

        #Royal flush, straight flush, flush
        if 5 in self.suitCount:

            #royal flush
            if self.rankCount[-5:] == [1,1,1,1,1]: rank=10

            #straight flush
            elif straight: rank = 9

            #plain flush
            else: rank = 6

        #four of a kind
        elif 4 in self.rankCount: rank = 8

        #full house or three of a kind
        elif 3 in self.rankCount:

            #full house
            if 2 in self.rankCount: rank = 7

            #three of a kind
            else: rank = 4

        elif straight: rank = 5

        #two pair
        elif self.rankCount.count(2) == 2: rank = 3

        #one pair
        elif 2 in self.rankCount: rank = 2

        #high card
        else: rank = 1

        return(rank)

#Ensures that the exit string is printed in the proper place
def niceExit(_str):
    print(_str)
    exit()

def rankToName(_rank):
    if _rank == 10: s="Royal Flush"
    elif _rank == 9: s="Straight Flush"
    elif _rank == 8: s="Four of a Kind"
    elif _rank == 7: s="Full House"
    elif _rank == 6: s="Flush"
    elif _rank == 5: s="Straight"
    elif _rank == 4: s="Three of a Kind"
    elif _rank == 3: s="Two Pair"
    elif _rank == 2: s="One Pair"
    else: s="High Card"
    return(s)

def loadFile():
    playerHands = [[],[]]
    with open(os.getcwd()+'\\54.txt') as f:
        for line in f.readlines():
            currHands = line.rstrip('\n').split(' ')
            playerHands[0].append(Hand([Card(c[0],c[1]) for c in currHands[0:5]]))
            playerHands[1].append(Hand([Card(c[0],c[1]) for c in currHands[5:]]))
    return(playerHands)

def compareHands(_handOne, _handTwo):
    #print("pOne has "+rankToName(_handOne.ranking())+", and pTwo has "+rankToName(_handTwo.ranking()))
    winner = 0
    rOne = _handOne.ranking()
    rTwo = _handTwo.ranking()

    if rOne > rTwo:
        winner = 1
    elif rOne < rTwo:
        winner = 2
    else:
        #have to compare the same-ranked hands
        #we can assume that it is not the case that both players have equal flushes/straights ("there is a clear winner")
        oneHigh = 0
        twoHigh = 0

        if rOne == 10:
            niceExit("ERROR: P1 and P2 both have royal flushes")

        #straight flush - player with lower starting card loses
        #cycle through the rank count and find the lowest value
        if rOne == 9:
            for i in range(13):
                if _handOne.rankCount[i] == 1 and _handTwo.rankCount[i] == 1:
                    niceExit("ERROR: P1 and P2 have identical straight flushes")
                elif _handOne.rankCount[i] == 1:
                    winner = 2
                    break
                elif _handTwo.rankCount[i] == 1:
                    winner = 1
                    break

        #four of a kind - only one extra possible card
        if rOne == 8:
            oneHigh = _handOne.rankCount.index(1)
            twoHigh = _handTwo.rankCount.index(1)

            if oneHigh > twoHigh:
                winner = 1
            elif twoHigh > oneHigh:
                winner = 2
            else:
                niceExit("ERROR: P1 and P2 have identical four-of-a-kinds")

        #full house
        elif rOne == 7:
            oneUpper = _handOne.rankCount.index(3)
            oneLower = _handOne.rankCount.index(2)
            twoUpper = _handTwo.rankCount.index(3)
            twoLower = _handTwo.rankCount.index(2)

            if oneUpper > twoUpper:
                winner = 1
            elif oneUpper < twoUpper:
                winner = 2
            else:
                if oneLower > twoLower:
                    winner = 1
                elif oneLower < twoLower:
                    winner = 2
                else:
                    niceExit("ERROR: P1 and P2 have identical full houses")

        #flush
        elif rOne == 6:
            i = 12
            #get the highest rank card where the hands don't match
            while _handOne.rankCount[i] == _handTwo.rankCount[i]:
                i -= 1

            if _handOne.rankCount[i] > _handTwo.rankCount[i]:
                winner = 1
            elif _handOne.rankCount[i] < _handTwo.rankCount[i]:
                winner = 2

        #straight
        elif rOne == 5:
            #get the lowest rank card of either hand
            for i in range(13):
                if _handOne.rankCount[i] == 1 and _handTwo.rankCount[i] == 1:
                    niceExit("ERROR: P1 and P2 have identical straights")
                elif _handOne.rankCount[i] == 1:
                    winner = 2
                    break
                elif _handTwo.rankCount[i] == 1:
                    winner = 1
                    break

        #three of a kind
        elif rOne == 4:
            oneTriple = _handOne.rankCount.index(3)
            twoTriple = _handOne.rankCount.index(3)
            oneExtras = sorted([x for x in range(13) if (_handOne.rankCount[x] == 1 or _handOne.rankCount[x] == 2)])
            twoExtras = sorted([x for x in range(13) if (_handTwo.rankCount[x] == 1 or _handTwo.rankCount[x] == 2)])
            #oneExtras = sorted([x for x in _handOne.rankCount if (x == 1 or x == 2)])
            #twoExtras = sorted([x for x in _handTwo.rankCount if (x == 1 or x == 2)])

            if oneTriple == twoTriple:
                i = 1
                while oneExtras[i] == twoExtras[i]:
                    i -= 1

                if _handOne.rankCount[oneExtras[i]] > _handTwo.rankCount[twoExtras[i]]:
                    winner = 1
                elif _handOne.rankCount[oneExtras[i]] < _handTwo.rankCount[twoExtras[i]]:
                    winner = 2

        #two pair
        elif rOne == 3:
            oneFirstPair = _handOne.rankCount.index(2)
            oneSecondPair = _handOne.rankCount[::-1].index(2)
            oneHigh = _handOne.rankCount.index(1)
            twoFirstPair = _handTwo.rankCount.index(2)
            twoSecondPair = _handTwo.rankCount[::-1].index(2)
            twoHigh = _handTwo.rankCount.index(1)

            oneHighPair = max(oneFirstPair, oneSecondPair)
            oneLowPair = min(oneFirstPair, oneSecondPair)
            twoHighPair = max(twoFirstPair, twoSecondPair)
            twoLowPair = min(twoFirstPair, twoSecondPair)

            if oneHighPair > twoHighPair:
                winner = 1
            elif oneHighPair < twoHighPair:
                winner = 2
            else:
                if oneLowPair > twoLowPair:
                    winner = 1
                elif oneLowPair < twoLowPair:
                    winner = 2
                else:
                    if oneHigh > twoHigh:
                        winner = 1
                    elif oneHigh < twoHigh:
                        winner = 2
                    else:
                        niceExit("ERROR: P1 and P2 have identical two pairs")

        #one pair
        elif rOne == 2:
            onePair = _handOne.rankCount.index(2)
            twoPair = _handTwo.rankCount.index(2)
            oneExtras = sorted([x for x in range(13) if (_handOne.rankCount[x] == 1)])
            twoExtras = sorted([x for x in range(13) if (_handTwo.rankCount[x] == 1)])

            if onePair > twoPair:
                winner = 1
            elif onePair < twoPair:
                winner = 2
            else:
                i = 2
                while oneExtras[i] == twoExtras[i]:
                    i -= 1

                if oneExtras[i] > twoExtras[i]:
                    winner = 1
                elif oneExtras[i] < twoExtras[i]:
                    winner = 2
                else:
                    niceExit("ERROR: P1 and P2 have identical one pairs")

        #high card
        elif rOne == 1:
            i = 12
            while _handOne.rankCount[i] == _handTwo.rankCount[i]:
                i -= 1

            if _handOne.rankCount[i] > _handTwo.rankCount[i]:
                winner = 1
            elif _handOne.rankCount[i] < _handTwo.rankCount[i]:
                winner = 2
            else:
                niceExit("ERROR: P1 and P2 have identical high card hands")

        else:
            niceExit("ERROR: Unknown ranks "+str(rOne)+","+str(rTwo))

    return(winner)


hands = loadFile()
pOneHands = hands[0]
pTwoHands = hands[1]

pOneWins = 0
for z in range(1000):
    if compareHands(pOneHands[z], pTwoHands[z]) == 1:
        pOneWins += 1
print("Player one won "+str(pOneWins)+" times")
