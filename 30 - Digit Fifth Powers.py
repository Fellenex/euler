import math

bigSum = 0
for i in range(2,1000000):
    s = str(i)

    digSum = 0
    for j in range(len(s)):
        digSum += int(math.pow(int(s[j]),5))

    if digSum == i:
        print(i)
        bigSum += digSum

print(bigSum)
