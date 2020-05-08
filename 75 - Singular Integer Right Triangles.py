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

for u in range(1,1000):
	for v in range(1,1000):
		if not(u <= v):
			a = u*u - v*v
			b = 2*u*v
			c = u*u + v*v
			print("Triple: "+str(a)+","+str(b)+","+str(c))

			#stop the v-loop early and move onto the next u-loop iteration if the length is too great
			if a+b+c > maxLength: break

			#add to the by-length dictionary, or start a list if this is the first
			if a+b+c in triangleDict:
				triangleDict[a+b+c].append((a,b,c))
			else:
				triangleDict[a+b+c] = [(a,b,c)]

#only count the lengths where the
uniqueLengthSpecialTriangles = [triangleDict[ell] for ell in triangleDict if len(triangleDict[ell]) == 1]

print(triangleDict)
print(len(triangleDict))
print(uniqueLengthSpecialTriangles)
print(len(uniqueLengthSpecialTriangles))
