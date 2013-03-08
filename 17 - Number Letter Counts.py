import math

#~ If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
#~ there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#~ If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#~ how many letters would be used?

#~ NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
#~ letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
#~ numbers is in compliance with British usage.

numToCount = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
		11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
		20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:10, 1000:8}

n = 1000
sum = 0

for i in range(1, n):
	numString = str(i)
	if (int(numString[-1]) != 0):
		sum += numToCount[int(numString[-1])]
	
	if (int(numString[-2:]) > 9):
		#from 11 to 19 (the weird ones)
		if (int(numString[-2:]) < 20):
			sum += numToCount[int(numString[-2:])]
			#this offset accounts for a ones column sum addition
			#when there is also a "-teen" sum addition
			if (int(numString[-1]) != 0):
				sum -= numToCount[int(numString[-1])]
		else:
			sum += numToCount[int(numString[-2])*10]
	
			
	if (len(numString) == 3):
		#the multiple of a hundred that the number is
		sum += numToCount[int(numString[-3])]
		
		#if the number is exactly a multiple of 100, then it doesn't require the 'and' after 'hundred'
		if (numString[-2:] != '00'):
			sum += numToCount[100]
		else:
			sum += numToCount[100] - 3
		
#adjusting for the character count of 'one thousand'
sum += numToCount[1]
sum += numToCount[1000]

print sum