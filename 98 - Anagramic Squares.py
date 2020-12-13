

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
squares = []
x=1
while len(str(x*x)) <= maxWordLength:
    squares.append(x*x)
    x+=1
