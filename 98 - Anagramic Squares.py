#Returns true/false indicating whether or not s1 and s2 are anagrams of each other.
def areAnAnagram(s1, s2):
    return(sorted(s1) == sorted(s2))


#Takes a list of strings and returns a list of lists, each containing the strings that are anagrams of each other.
def getAnagramEquivalencyClasses(stringList):
    equivalencyClasses = []

    #tracks which indices have had their equivalency class measured (avoid creating multiple identical classes)
    tracked = [False] * len(words)

    for i in range(len(words)):
        #if we've incremented i to an index we've already examined (when it was j, using a lower value for i), then skip this index i.
        if tracked[i]:
            continue

        #if we haven't already examined the word at index i, then do so.
        else:
            tracked[i] = True
            eqClass = [words[i]]

            for j in range(i+1, len(words)):
                #if we haven't already tracked j, then we check the anagram status between the ith word and jth word.
                if not tracked[j]:
                    if areAnAnagram(words[i], words[j]):
                        eqClass.append(words[j])

                        #we should only mark j as tracked when it is part of an equivalency class we have already defined.
                        #if we mark j as tracked here and it was not an anagram with i, then it won't be added to
                        #   any equivalency class in the anagrams list.
                        tracked[j] = True

            equivalencyClasses.append(eqClass)

    return equivalencyClasses


#Creates two dictionary mappings; one from characters -> digits, and the other from digits -> characters.
def getNumericalMapping(stringToMap, mappingNum):
    assert(len(stringToMap) == len(str(mappingNum)))

    #we use sets as the values in these dictionaries, because they will prevent multiple entries on the same char:digit mapping.
    #mapByChar and mapByDict are inversions of each other, which serves to determine conflicts more easily.
    mapByChar = dict()
    mapByNum = dict()

    #check to see if any letters would map to multiple numbers (e.g., 'aca' using 289 would map 'a' to both 2 and 9)
    for c in range(0,len(stringToMap)):
        try:
            mapByChar[stringToMap[c]].add(str(mappingNum)[c])
            #if we've successfully added to the set, then we have mapped the same letter stringToMap[c] to two different numbers.
        except KeyError:
            #if we haven't defined this letter's mapping yet, then we define it here.
            mapByChar[stringToMap[c]] = set(str(mappingNum)[c])

    #check to see if any numbers would be mapped to by multiple letters (e.g., 'act' using 121 would map both 'a' and 't' to 1)
    for d in range(0,len(str(mappingNum))):
        try:
            mapByNum[str(mappingNum)[d]].add(stringToMap[d])
            #if we've successfully added to the set, then we have mapped two different letters to the same digit mappingNum[c].
        except KeyError:
            #if we haven't defined what maps to this number yet, then we define it here.
            mapByNum[str(mappingNum)[d]] = set(stringToMap[d])

    return (mapByChar, mapByNum)


#Checks to see if a string c1 c2 ... ck can be mapped by an integer d1 d2 ... dl without conflicts.
def isValidNumericMapping(stringToMap, mappingNum):
    mapByChar, mapByNum = getNumericalMapping(stringToMap, mappingNum)

    #if either of mapByChar or mapByNum have a key with a set of size at least 2, then there is an overloading of the mapping.
    charsUnique = all([len(mapByChar[key]) <= 1 for key in mapByChar])
    digitsUnique = all([len(mapByNum[key]) <= 1 for key in mapByNum])

    #so then if all mappings have at most one entry, then this is a valid mapping for this word.
    return(charsUnique and digitsUnique)

#Turns a mapping like {'a' : {'2'}, ...} into a mapping like {'a' : '2', ...}
#NOTE: Assumes that there is only one value for each character key. if there are multiple, then it will not consider all of them.
def simplifyMapping(mappingDictWithSets):
    newMappingDict = dict()
    for key in mappingDictWithSets:
        newMappingDict[key] = mappingDictWithSets[key].pop()
    return(newMappingDict)


#Takes a string and a dictionary associating characters with digits.
def getMappedString(stringToMap, mappingDict):
    mappedString = ""
    for c in stringToMap:
        mappedString += mappingDict[c]
    return(mappedString)


words = []
with open('98.txt') as f:
    #the words all appear on the same line, but are split by commas.
    #we remove the first and last character of each word, since they are all outfixed by quotation marks.
    words = [x[1:-1] for x in f.read().split(',')]

#first we should split words into anagram equivalency classes
equivalencyClasses = getAnagramEquivalencyClasses(words)

#we only need to consider equivalency classes that have at least two elements. e.g., ['ACT', 'CAT'].
anagrams = [eqClass for eqClass in equivalencyClasses if len(eqClass) > 1]

#get the maximum length of any anagram
maxWordLength = max([len(anagramList[0]) for anagramList in anagrams])

#we preload all squares with a digital length at most the same length as the longest anagramic word.
#this way, we just check to see if the number exists in the list, rather than checking squareness later.
squares = [[]]

squareLength=0  #tracks the number of digits in the current square, so that we can split the squares by length.
x=1             #tracks the index of the square number
while len(str(x*x)) <= maxWordLength:
    if len(str(x*x)) > squareLength:
        squares.append([])  #add a new list for squares of this length
        squareLength = len(str(x*x))

    #add the current square number to the most recently added list (for squares of this length)
    squares[-1].append(x*x)
    x+=1


largestSquare = 1
#loop over each anagram equivalency class with at least two members
for eqClass in anagrams:
    numMappingsNeeded = len(eqClass)

    #try to find a square number whose mapping works with the first word
    for square in squares[len(eqClass[0])]:
        if isValidNumericMapping(eqClass[0], square):
            mapByChar, mapByNum = getNumericalMapping(eqClass[0], square)

            #since mapByChar and mapByNum are inversions of each other, we focus on the one that maps chars to digits.
            mapping = simplifyMapping(mapByChar)

            #Get the numbers created by mapping other strings in this anagram equivalency class using the mapping created by the first string.
            mappedEqClass = [int(getMappedString(s, mapping)) for s in eqClass]

            allMappingsAreSquares = True
            #checks to see that each of the numbers, created by mapping anagrams using this current mapping, are squares
            for d in mappedEqClass:
                if not(d in squares[len(eqClass[0])]):
                    allMappingsAreSquares = False

            #keep track of the largest anagramic square mapping we've seen so far.
            #make sure to consider all squares created by all strings in this equivalency class
            if allMappingsAreSquares:
                for sq in mappedEqClass:
                    largestSquare = max(largestSquare, sq)

print("Largest anagramic mapping uses %s" % largestSquare)
