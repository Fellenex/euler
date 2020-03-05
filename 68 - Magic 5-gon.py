solutionStrings = []

"""
since 10 has the smallest effect on the clockwise concatenation of 'gon-lines, we want it to be last
so then the vertex just clockwise of 10 is the smallest outside vertex (so that counting starts there)

10 + a + b == v1 + b + c
--> 10 + a == v1 + c
--> v1 == 10 + a - c
since v1 < 10, we get c > a

v4 + e + a == 10 + a + b
--> v4 + e == 10 + b
--> v4 - 10 == b - e
since v4 < 10, we get e > b

We also get
    v1 = 10 + a - c
    v4 = 10 + b - e
"""

#always e > b
for b in range(1,9):
    for e in range(b+1,10):

        #always c > a
        for a in range(1,9):
            for c in range(a+1,10):

                for d in range(1,10):
                    insideAssignment = [a,b,c,d,e]
                    unique = True
                    for x in range(1,10):
                        if insideAssignment.count(x) > 1:
                            unique = False

                    if unique:

                        #We can calculate two of the outside vertex values (based on the inside vertex values)
                        vOne = 10 + a - c
                        vFour = 10 + b - e

                        for vTwo in range(1,10):
                            for vThree in range(1,10):

                                totalAssignment = [a,b,c,d,e,vOne,vTwo,vThree,vFour]
                                unique = True
                                for x in range(1,10):
                                    if totalAssignment.count(x) > 1:
                                        unique = False

                                if unique:
                                    if (10+a+b) == (vOne+b+c) == (vTwo+c+d) == (vThree+d+e) == (vFour+e+a):
                                        solutionStrings.append(str(vOne)+str(b)+str(c)+str(vTwo)+str(c)+str(d)+str(vThree)+str(d)+str(e)+str(vFour)+str(e)+str(a)+"T"+str(a)+str(b))

solutions = []
print("Found "+str(len(solutionStrings))+" solutions")
for s in solutionStrings[::-1]:
    solutions.append([s[i*3:(i+1)*3] for i in range(5)])

rotatedSolutions = []
#Lucky for us, 'T' counts as larger than any numeric character.
#Rotate the list so that the element with the smallest starting value (the outside vertex) is the first element.
for s in solutions:
    for e in range(len(s)):

        if s[e] == min(s):
            rotatedSolutions.append(s[e:]+s[:e])

collapsedSolutions = sorted(["".join(rs) for rs in rotatedSolutions])
print("The largest string for a magic 5-gon is "+str(collapsedSolutions[-1]))
