"""
In England the currency is made up of pounds, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, 1 (100p) and 2 (200p).

It is possible to make 2 pounds in the following way:

    1x1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can 2 pounds be made using any number of coins?
"""

"""


"""

def howManyWays(_rem, _coins, _ways):
    if _rem==0:
        return []

    for coin in _coins:
        #print _rem, coin

        if _rem >= coin:
            ways = [functionalAppend(x,coin) for x in _ways]
            howManyWays(_rem-coin,_coins,ways)

        else:
            ways = []

    return ways

def functionalAppend(_list,_item):
    _list.append(_item)
    return _list

#print [functionalAppend(x,5) for x in [[1,2],[3,4],[5,5],[],[6,[7],]]]





ways = howManyWays(5, [200,100,50,20,10,5,2,1], [])

#collapse unnecessary outer lists
ways = [item for sublist in ways for item in sublist]

print ways
print

for w in ways:
    if type(w) is list:
        print "\n\t"+str(w)
    else:
        print ", "+str(w)
