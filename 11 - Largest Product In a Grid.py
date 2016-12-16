#Determines the greatest product in any legal direction, based on a specific row/column starting point.
#
#Parameters:
#	_rows: A 2-dimensional list containing Numerics
#	_rowIndex: An integer, representing the current row's index
#	_colIndex: An integer, representign the current column's index
#
#Return value:
#	The maximum product in any direction from the current starting point at rows[_rowIndex][_colIndex]
#
def adjacentProducts(_rows, _rowIndex, _colIndex):
	currProducts = []
	boundsList = [True,True,True,True,True,True,True,True] #length 8, one for each of the possible directions

	if _colIndex < 3:
		#We can't go left, or diag down/up left
		boundsList[1] = False
		boundsList[5] = False
		boundsList[7] = False

	if len(_rows[0]) - _colIndex < 4:
		#We can't go right, or diag down/up right
		boundsList[0] = False
		boundsList[4] = False
		boundsList[6] = False


	if _rowIndex < 3:
		#We can't go up, or diagonally up left/right
		boundsList[3] = False
		boundsList[6] = False
		boundsList[7] = False

	if len(_rows)-_rowIndex < 4:
		#We can't go down, or diagonally down left/right
		boundsList[2] = False
		boundsList[4] = False
		boundsList[5] = False


	#Directly right
	if boundsList[0]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex][_colIndex+1]*_rows[_rowIndex][_colIndex+2]*_rows[_rowIndex][_colIndex+3])
		
	#Directly left
	if boundsList[1]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex][_colIndex-1]*_rows[_rowIndex][_colIndex-2]*_rows[_rowIndex][_colIndex-3])


	#Directly down
	if boundsList[2]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex+1][_colIndex]*_rows[_rowIndex+2][_colIndex]*_rows[_rowIndex+3][_colIndex])
	#Directly up
	if boundsList[3]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex-1][_colIndex]*_rows[_rowIndex-2][_colIndex]*_rows[_rowIndex-3][_colIndex])


	#Diagonally down/right
	if boundsList[4]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex+1][_colIndex+1]*_rows[_rowIndex+2][_colIndex+2]*_rows[_rowIndex+3][_colIndex+3])
	#Diagonally down/left
	if boundsList[5]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex+1][_colIndex-1]*_rows[_rowIndex+2][_colIndex-2]*_rows[_rowIndex+3][_colIndex-3])

	#Diagonally up/right
	if boundsList[6]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex-1][_colIndex+1]*_rows[_rowIndex-2][_colIndex+2]*_rows[_rowIndex-3][_colIndex+3])
	#Diagonally up/left
	if boundsList[7]:
		currProducts.append(_rows[_rowIndex][_colIndex]*_rows[_rowIndex-1][_colIndex-1]*_rows[_rowIndex-2][_colIndex-2]*_rows[_rowIndex-3][_colIndex-3])

	return max(currProducts)


def main():
	maxProduct = 0
	rows = []

	#First we read from the file and split the numbers into individual cells in a 2-dimensional list.
	with open('11.txt', 'r') as f:
		for line in f:
			rows.append([int(numString) for numString in line.rstrip('\n').split()])
	numRows = len(rows)
	rowLength = len(rows[0])

	#Then we successively look for the greatest product from every starting point.
	for rowIndex in range(numRows):
		for colIndex in range(rowLength):
			maxProduct = max(maxProduct, adjacentProducts(rows, rowIndex, colIndex))

	print maxProduct

main()