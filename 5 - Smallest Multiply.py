#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 20
temp = 0
while(1):
	for i in range(1, 21):
		if (x%i == 0):
			temp +=1
	if temp == 20:
		print x
		break
	temp = 0
	x +=1