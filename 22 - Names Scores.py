illFormattedNames = []
wellFormattedNames = []
letterScore = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
namesAndValues = {}

import os

print os.getcwd()

#only one line in our formatted text file.
with open("names.txt", 'r') as namesFile:
	for line in namesFile:
		wholeString = line

#names are separated by commas, and are all encapsulated in quotation marks.
illFormattedNames = wholeString.split(',')
for name in illFormattedNames:
	formattedName = name.rstrip('"')
	formattedName = formattedName.lstrip('"')
	formattedName = formattedName.rstrip('\n')
	print formattedName
	wellFormattedNames.append(formattedName)

print wellFormattedNames
for name in wellFormattedNames:
	sum = 0
	for char in range(len(name)):
		print name[char]
		sum += letterScore[char]
	namesAndValues[name] = sum

for i in namesAndValues:
	print i
