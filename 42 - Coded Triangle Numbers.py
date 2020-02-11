"""
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

#Returns a list of all of the triangle numbers up to n (or until just after n)
def triangleNumbersUpTo(n):
    i = 1
    t = 1
    tNums = []
    while t < n:
        t = (0.5)*i * (i+1)
        tNums.append(int(t))
        i+=1
    return(tNums)

#Gets the sum of a word for its encoding.
#   e.g., SKY = 19 + 11 + 25 = 55
def encodedWordSize(word):
    return sum([ord(c)-charEncodingOffset for c in word])

#Define the mapping A->1, all the way to Z->26
charEncodingOffset = 64
letterDict = dict()
for i in range(65,91): letterDict[chr(i)] = i-charEncodingOffset

with open('42.txt','r') as f:
    lines = f.read().split(',')

#Remove the quotation marks prefixing and suffixing each word
strippedWords = [line[1:-1] for line in lines]

#Get the largest triangle number we'll have to compute
maxWordSize = max([encodedWordSize(word) for word in strippedWords])
triangleNumbers = triangleNumbersUpTo(maxWordSize)


triangleWords = []
for word in strippedWords:
    if encodedWordSize(word) in triangleNumbers:
        triangleWords.append(word)

print(triangleWords)
print(len(triangleWords))
