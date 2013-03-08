#~ The following iterative sequence is defined for the set of positive integers:

#~ n  n/2 (n is even)
#~ n  3n + 1 (n is odd)

#~ Using the rule above and starting with 13, we generate the following sequence:

#~ 13  40  20  10  5  16  8  4  2  1
#~ It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#~ Although it has not been proved yet (Collatz Problem),
#~ it is thought that all starting numbers finish at 1.

#~ Which starting number, under one million, produces the longest chain?

#~ NOTE: Once the chain starts the terms are allowed to go above one million.

#basic recursive algorithm for the collatz sequence
#appends the values to a list to store them for
#outside of the function properties
def collatz(n):
	collatzList.append(n)
	if n == 1:
		return 1
	if n%2 == 0:
		return collatz((n/2))
	else:
		return collatz(((n*3)+1))
		
collatzList = []
i = 1
max = 0
start = 0
while (1):
	if i > 1000000:
		break
	else:
		collatzList = []
		collatz(i)
		if len(collatzList) > max:
			max = len(collatzList)
			start = i
	i+=1
print start
print max
	