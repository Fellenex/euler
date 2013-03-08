#~ By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#~ What is the 10 001st prime number?

def check_Prime(n):
	for i in range(n-1, 1, -1):
		if ((n%i) == 0):
			return False
	primeList.append(n)
	return True
	
primeList = []
x = 1
while(1):
	if (x%2 != 0):
		check_Prime(x)
		if len(primeList) == 10001:
			break
	x+=1

print primeList
print primeList[-1]