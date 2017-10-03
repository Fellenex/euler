#A permutation is an ordered arrangement of objects.
#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
#The lexicographic permutations of 0, 1 and 2 are:
	#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#Proof:
#With A={0}, there is 1 lexicographic permutation
#With A={0,1}, there are 2 lexicographic permutations
#With A={0,1,2}, there are 6 different lexicographic permutations
#With A={0, ..., n-1}, there are n! different lexicographic permutations

#So with n=10, there are 10! (3628800) permutations.

#To find the millionth one, we separate them by order
#With A={0,1}, there is 1 permutation for each starting character; 2*1=2
#With A={0,1,2}, there are 2 permutations for each starting character; 3*2=6
#With A={0,1,2,3}, there are 6 permutations for each starting character; 4*6=24
#With A={0, ..., n-1}, there are (n-1)! different permutations for each starting character.

#So in the ordered 10! permutations:
	#The first 9! start with 0
	#The second 9! start with 1
	#...
	#The last 9! start with 9.

#Since 9! is 362880, 2*9! < 1'000'000, and 3*9! > 1'000'000.
#So the 1 millionth permutation will start with a 2.
#'2013456789' will be the 725'760th permutation, since it is 2*9!+1
