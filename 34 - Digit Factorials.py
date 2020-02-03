"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


factMemos = dict()
factMemos[0] = 1
factMemos[1] = 1

def memoizedFactorial(n):
    try:
        return factMemos[n]
    except KeyError:
        return n*memoizedFactorial(n-1)

for i in range(10):
    factMemos[i] = memoizedFactorial(i)

factorialEqualsDigitSum = []
for i in range(3,factMemos[9]*3):
    splitFactSum = 0
    for c in str(i):
        #print("\t"+c)
        splitFactSum += memoizedFactorial(int(c))

    if splitFactSum == i:
        factorialEqualsDigitSum.append(i)

print(factorialEqualsDigitSum)
