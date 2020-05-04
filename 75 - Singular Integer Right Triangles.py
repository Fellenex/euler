#for ell in range(12,15000000):
for ell in range(12,1000):
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
