"""
#for ell in range(12,15000000):
for ell in range(12,50):
	ways = 0
	for a in range(1,ell):
		for b in range(a+1,ell):
			for c in range(b+1,ell):
				if a+b+c == ell:
					ways += 1

				if a+b+c >= ell:
					break

			if a+b >= ell:
				break

print(ways)
"""

triangleDict = dict()
maxLength = 15000000

for u in range(1,2500):
	for v in range(u,2500):
		a = u*u - v*v
		b = 2*u*v
		c = u*u + v*v
		#print("Triple: "+str(a)+","+str(b)+","+str(c))

		length = a+b+c
		#stop the v-loop early and move onto the next u-loop iteration if the length is too great
		if (a+b+c) <= maxLength:
			print("Iterating onto "+str(length))
			#add to the by-length dictionary, or initialize it if this is the first.
			if length in triangleDict:
				triangleDict[length] += 1 #.append((a,b,c))
			else:
				triangleDict[length] = 1 #[(a,b,c)]

print("Yasss")
#only count the lengths where there is only one special right triangle with that perimetre
uniqueLengthSpecialTriangles = [triangleDict[ell] for ell in triangleDict if triangleDict[ell] == 1]

print(triangleDict)
print(len(triangleDict))
print(uniqueLengthSpecialTriangles)
print(len(uniqueLengthSpecialTriangles))
