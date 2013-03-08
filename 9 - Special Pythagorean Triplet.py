#~ A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

#~ a2 + b2 = c2
#~ For example, 32 + 42 = 9 + 16 = 25 = 52.

#~ There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#~ Find the product abc.

listA = []
listB = []
listC = []


for i in range(1, 350):
	for j in range(1, 350):
		for k in range(1, 350):
			if ((i*i)+(j*j) == (k*k)):
				listA.append(i)
				listB.append(j)
				listC.append(k)

for i in range(len(listA)):
	if (listA[i] + listB[i] + listC[i] == 1000):
		print listA[i]
		print listB[i]
		print listC[i]
		print