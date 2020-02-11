#Returns a list of the first _n triangular numbers
def generateTriangulars(_n):
    return([int(i*(i+1)/2) for i in range(1,_n+1)])

#Returns a list of the first _n pentagonal numbers
def generatePentagonals(_n):
    return([int(i*(3*i-1)/2) for i in range(1,_n+1)])

#Returns a list of the first _n hexagonal numbers
def generateHexagonals(_n):
    return([int(i*(2*i - 1)) for i in range(1,_n+1)])
