#~ A palindromic number reads the same both ways.
#~ The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
#~ Find the largest palindrome made from the product of two 3-digit numbers.

#This program uses nested loops to test all multiplicative values from 100 to 999
#It then checks to see if the product is a palindrome, then compares it to the old maximum palindrome
max = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		product = i*j
		strProd = str(product)
		if len(strProd) == 5:
			if (strProd[:2] == strProd[-1:2:-1]):
				if product > max:
					max = product
		if len(strProd) == 6:
			if (strProd[:3] == strProd[-1:2:-1]):
				if product > max:
					max = product

print max
