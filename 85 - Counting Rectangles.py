"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""


#Gets the total number of rectangles of a specified size that can fit in a space of a specific area
def countRectanglesBySize(_rectX, _rectY, _spaceX, _spaceY):
    count = 0
    if _rectX <= _spaceX and _rectY <= _spaceY:
        #create a sliding window across the space

        xSlide = _spaceX - _rectX
        ySlide = _spaceY - _rectY

        count = (1 + xSlide) * (1 + ySlide)

    return(count)

#Gets the total number of rectangles of any size that can fit into a space of a specific area
def countRectanglesByArea(_spaceX,_spaceY):
    total = 0
    for x in range(1, _spaceX+1):
        for y in range(1, _spaceY+1):
            total += countRectanglesBySize(x, y, _spaceX, _spaceY)
    return(total)


closestPair = (0,0)
closestDiff = 2000000
target = 2000000

for spaceX in range(1,80):
    for spaceY in range(spaceX,80):
        curr = countRectanglesByArea(spaceX, spaceY)
        #rectMemos[(spaceX, spaceY)] = curr

        if abs(target - curr) < closestDiff:
            print(str(curr)+" is closer to "+str(target)+" than "+str(closestPair))
            closestPair = (spaceX, spaceY)
            closestDiff = abs(target - curr)

print(closestDiff)
print(closestPair)
print(closestPair[0]*closestPair[1])
