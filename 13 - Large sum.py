#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#See 13.txt for the numbers


#Read in the numbers as strings
rows=[]
with open('13.txt', 'r') as f:
    for line in f:
        rows.append(line.rstrip('\n'))
