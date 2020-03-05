solutions = []

"""
since 10 has the smallest effect on the clockwise concatenation of 'gon-lines, we want it to be last
so then the vertex just clockwise of 10 is the smallest outside vertex (so that counting starts there)

10 + a + b == v1 + b + c
--> 10 + a == v1 + c
--> v1 == 10 + a - c
since v1 < 10, we get c > a

v1 + b + c == v2 + c + d
--> v1 + b == v2 + d
--> v1 - v2 + b == d
--> v1 - v2 == d - b
v1 is the smallest outside vertex, then v1 - v2 is negative
then we get d - b is also negative, so b > d

v2 + c + d == v3 + d + e
--> v2 + c == v3 + e
--> v2 - v3 + c == e
--> v2 - v3 == e - c
since we want to maximize the string concatenation, v2 should be the largest outside vertex
so then v2 > v3, meaning v2 - v3 is positive
then e - c is also positive, so e > c

v3 + d + e == v4 + e + a
--> v3 + d == v4 + a
--> v3 - v4 + d == a
--> v3 - v4 == a - d
similarly with v2 and v3, v3 being larger has a greater effect on the string concatenation's total value
so then v3 > v4, meaning v3 - v4 is positive
then a - d is also positive, so a > d

v4 + e + a == 10 + a + b
--> v4 + e == 10 + b
--> v4 - 10 + e == b
--> v4 - 10 == b - e
since 10 is the maximum value, v4 must be smaller
so then v4 - 10 is negative
then b - e is also negative, so e > b


Combining these together, we get the following two properties:
    e > c > a > d
    e > b > d


so one of the following must hold:
    e > b > c > a > d
    e > c > b > a > d
    e > c > a > b > d

"""

#TODO: is it possible that we can't assume that 10 is the "final" line in the clockwise circulation?

for vOne in range(1,6+1):
    for vFour in range(vOne+1,7+1):
        for vThree in range(vFour+1,8+1):
            for vTwo in range(vThree+1,9+1):

                for d in range(1,5+1):
                    for e in range(d+4,9+1):

                        #The middle range, we don't know how b fits in with a,b, but we do know c > a
                        #Even if we change a,b,c,d,e to be any value between [1,9], it still finds no solutions
                        for b in range(2,8+1):
                            for a in range(2,8+1):
                                for c in range(a+1,8+1):

                                    assignment = [vOne,vFour,vThree,vTwo,d,e,b,a,c]
                                    unique = True
                                    for x in range(1,10):
                                        if assignment.count(x) > 1:
                                            unique = False

                                    if unique:
                                        if (10+a+b) == (vOne+b+c) == (vTwo+c+d) == (vThree+d+e) == (vFour+e+a):
                                            solutions.append(str(vOne)+str(b)+str(c)+str(vTwo)+str(c)+str(d)+str(vThree)+str(d)+str(e)+str(vFour)+str(e)+str(a)+"T"+str(a)+str(b))

print("Found "+str(len(solutions))+" solutions")
for s in solutions[::-1]:
    print([s[i*3:(i+1)*3] for i in range(5)])
#All the solutions it's coming up with have duplicate elements throughout
