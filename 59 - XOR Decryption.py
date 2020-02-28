"""
Each character on a computer is assigned a unique code and the preferred standard is
    ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
    then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
    restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
    and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations,
    and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users,
    so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely,
    the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security,
    but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
    Using p059_cipher.txt (right click and 'Save Link/Target As...'),
    a file containing the encrypted ASCII codes,
    and the knowledge that the plain text must contain common English words,
    decrypt the message and find the sum of the ASCII values in the original text.
"""

import os
import math
import itertools

encryptionLength = 3
encryptionIndices = [0]*encryptionLength
letters = []
with open(os.getcwd()+'\\59.txt') as f:
    letters = [int(x) for x in f.readline().split(',')]

passwordRepetitions = int(math.floor(len(letters)/(encryptionLength*1.0)))
leftover = len(letters) % encryptionLength

#The numeric ranges for ascii characters to use as a password
passwordRanges = range(97,123)

#The valid ascii characters that could be in the file
#(includes tab, newline, carriage return, space, and other punctuations.
validChars = [chr(x) for x in [9,10,13,32] + range(33,127)]


#Setup the lists into which we'll save possible encryption characters for each letter of the passcode
encryptionCharacterPossibilities = []
for i in range(encryptionLength):
    encryptionCharacterPossibilities.append([])


for i in range(encryptionLength):
    for c in passwordRanges:

        #Encode all of the characters (based on password's length) that will use character c in position i
        encoding = [chr(x ^ c) for x in letters[i:passwordRepetitions*encryptionLength:encryptionLength]]

        #Check to make sure that each of c's encoded characters are valid english text
        validity = True
        for enc in encoding:
            if not(enc in validChars):
                validity = False
                break

        if validity:
            encryptionCharacterPossibilities[i].append(chr(c))
            #print("Encryption char "+chr(c)+" is a possibility for pass char "+str(i))


#Collapse the encryptionLength lists into one list of possible encryption words
encryptionWordPossibilities = encryptionCharacterPossibilities[0]
for i in range(1,encryptionLength):
    encryptionWordPossibilities = [x[0]+x[1] for x in itertools.product(encryptionWordPossibilities, encryptionCharacterPossibilities[i])]
print("There are "+str(len(encryptionWordPossibilities))+" possible encryption passwords of length "+str(encryptionLength))


#Now encrypt the text with each of the possible passwords, saving it.
for possiblePassword in encryptionWordPossibilities:
    currentDecryption = []
    for i in range(passwordRepetitions):

        for j in range(encryptionLength):
            #print("Adding "+chr(letters[(i*encryptionLength)+j] ^ ord(possiblePassword[j]))+" to current encryption")
            currentDecryption.append(chr(letters[(i*encryptionLength)+j] ^ ord(possiblePassword[j])))

    #Write the encrypted text
    with open(os.getcwd()+'\\59\\'+possiblePassword+'.txt', 'w') as f:
        for c in currentDecryption:
            f.write(c)

    #Found answer by inspection
    if possiblePassword == "exp":
        print(sum([ord(c) for c in currentDecryption]))
