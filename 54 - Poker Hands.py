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

def compareHands(_handOne, _handTwo):
    print("Pone has "+rankToName(_handOne.ranking())+", and ptwo has "+rankToName(_handTwo.ranking()))
    winner = 0
    if _handOne.ranking() > _handTwo.ranking():
        winner = 1
    elif _handOne.ranking() < _handTwo.ranking():
        winner = 2
    else:
        #have to compare the same hands

        #we can assume that it is not the case that both players have equal flushes/straights ("there is a clear winner")

        #four of a kind comparison + high extra card comparison
        #full house 3+2 comparison
        #three of a kind + high extra card(s) comparison
        #two pair comparison
        #one pair comparison
        #high card comparison


pOneRaw = ["8S", "9S", "TS", "JS", "QS"]
pTwoRaw = ["2C", "3S", "8S", "8D", "TD"]

pOneHands = [["5H", "5C", "6S", "7S", "KD"], ["5D", "8C", "9S", "JS", "AC"], ["2D", "9C", "AS", "AH", "AC"], ["4D", "6S", "9H", "QH", "QC"], ["2H", "2D", "4C", "4D", "4S"]]
pTwoHands = [["2C", "3S", "8S", "8D", "TD"], ["2C", "5C", "7D", "8S", "QH"], ["3D", "6D", "7D", "TD", "QD"], ["3D", "6D", "7H", "QD", "QS"], ["3C", "3D", "3S", "9S", "9D"]]

for i in range(5):
    h = Hand([Card(c[0],c[1]) for c in pOneHands[i]])
    k = Hand([Card(c[0],c[1]) for c in pTwoHands[i]])
    compareHands(h,k)



#h = Hand([Card(c[0],c[1]) for c in pOneRaw])
#k = Hand([Card(c[0],c[1]) for c in pTwoRaw])
