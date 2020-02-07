"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

fractionSolutions = []

for n in range(10,100):
    for d in range(n+1,100):
        nS = str(n)
        nD = str(d)

        #skip 0-cancellable fractions (considered by the problem to be trivial)
        if nS[1]=='0' and nD[1]=='0':
            pass
        else:
            frac = (n*1.0)/d

            if nS[0] == nD[0]:
                #numerator and denominator share the first digit

                #avoid dividing by zero
                if not(nD[1] == '0'):
                    #print(n,d)
                    if frac == (int(nS[1])*1.0)/int(nD[1]):
                        fractionSolutions.append((n,d))

            elif nS[0] == nD[1]:
                #numerator's first digit and denominator's last digit are the same

                #avoid dividing by zero
                if not(nD[0] == '0'):
                    if frac == (int(nS[1])*1.0)/int(nD[0]):
                        fractionSolutions.append((n,d))

            elif nS[1] == nD[0]:
                #numerator's last digit and denominator's first digit are the same

                #avoid dividing by zero
                if not(nD[1] == '0'):
                    #print(n,d)
                    if n == 49:
                        print(n,d)
                        print((n*1.0)/d)
                        print(int(nS[1])*1.0)
                        print(int(nD[0]))
                        print((int(nS[1])*1.0)/int(nD[0]))
                        print((int(nS[0])*1.0)/int(nD[1]))
                        print
                    if frac == (int(nS[0])*1.0)/int(nD[1]):
                        fractionSolutions.append((n,d))

            elif nS[1] == nD[1]:
                #numerator and denominator share the last digit

                #avoid dividing by zero
                if not(nD[0] == '0'):
                    if frac == (int(nS[0])*1.0)/int(nD[0]):
                        fractionSolutions.append((n,d))

print(fractionSolutions)
prod = 1
for f in fractionSolutions:
    prod *= (f[0]*1.0)/f[1]

print(prod)
