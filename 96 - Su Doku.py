class suNode:
    def __init__(self, value=0):
        self.value = int(value)

        #we initialize empty sudoku nodes with a value of 0
        if self.value == 0:
            self.possibilities = list(range(1,10))
        else:
            self.possibilities = []

    def __str__(self):
        return str(self.value)

    def numPossibilities(self):
        return len(self.possibilities)

class suPuzzle:
    BOARD_SIZE = 9

    def __init__(self, rows):
        self.rows = rows

        self.cols = []
        for c in range(suPuzzle.BOARD_SIZE):
            column = []
            for row in rows:
                column.append(row[c])
            self.cols.append(column)


        #TODO: generalizable offsets for different board sizes when breaking up into squares
        self.squs = []
        #square-row offset x1
        for x in range(0, 7, 3):

            #column indices j
            for j in range(0, 7, 3):
                square = []

                #row indices i
                for i in range(3):
                    square += self.rows[i+x][j:j+3]
                self.squs.append(square)

        self.rowPossibilities = []
        self.colPossibilities = []
        self.sqPossibilities = []
        for r in range(suPuzzle.BOARD_SIZE):
            self.rowPossibilities.append(list(range(1,suPuzzle.BOARD_SIZE+1)))
            self.colPossibilities.append(list(range(1,suPuzzle.BOARD_SIZE+1)))
            self.sqPossibilities.append(list(range(1,suPuzzle.BOARD_SIZE+1)))

        self.updatePossibilities()



    def __str__(self):
        suString = ""
        for row in self.rows:
            rString = ""
            for cell in row:
                rString += str(cell.value)
            suString += rString+'\n'
        return(suString[:-1])   #cut off the trailing new-line


    #for a specified row r and column c, returns the square index of that cell.
    #squares are counted left-right, top-bottom. e.g., the 6th square is for rows 3,4,5 and cols 6,7,8 (with 0-indexing)
    def getSquareNumber(self, r, c):
        assert(0 <= r <= 8 and 0 <= c <= 8)

        if r < 3:
            if c < 3: number = 0
            elif c < 6: number = 1
            else: number = 2
        elif r < 6:
            if c < 3: number = 3
            elif c < 6: number = 4
            else: number = 5
        else:
            if c < 3: number = 6
            elif c < 6: number = 7
            else: number = 8

        return(number)


    #updates the row, column, and square trackers for what numbers could possibly still be used
    def updatePossibilities(self):
        #update the possibilities row- and column-wise
        for r in range(suPuzzle.BOARD_SIZE):
            for c in range(suPuzzle.BOARD_SIZE):
                try:
                    self.rowPossibilities[r].remove(self.rows[r][c].value)
                    self.colPossibilities[c].remove(self.cols[c][r].value)
                    #print("Removing %s,%s from row %s and col %s" % (self.rows[r][c].value, self.cols[c][r].value, r, c))
                except ValueError:
                    #if we couldn't remove it, don't worry about it
                    pass

        #update the possibilities square-wise
        for sq in range(suPuzzle.BOARD_SIZE):
            for cell in range(suPuzzle.BOARD_SIZE):
                try:
                    self.sqPossibilities[sq].remove(self.squs[sq][cell].value)
                    #print("removing %s from sq %s" % (self.squs[sq][cell].value, sq))
                except ValueError:
                    #if we couldn't remove it, don't worry about it
                    pass

        #update the possibilities cell-wise
        for r in range(suPuzzle.BOARD_SIZE):
            for c in range(suPuzzle.BOARD_SIZE):
                self.rows[r][c].possibilities = [v for v in self.rows[r][c].possibilities if
                    (v in self.rowPossibilities[r] and
                    v in self.colPossibilities[c] and
                    v in self.sqPossibilities[self.getSquareNumber(r,c)])
                    ]


    #returns boolean indicating whether or not all cells are filled in
    def isComplete(self):
        complete = True
        for r in range(suPuzzle.BOARD_SIZE):
            for c in range(suPuzzle.BOARD_SIZE):
                if self.rows[r][c].value == 0:
                    complete = False
        return(complete)

    #returns boolean indicating whether or there is no clashing among any cells
    def isValidSolution():
        pass



#a list of 2d lists, each containing the rows for a sudoku puzzle.
sudokus = []
with open('euler//96.txt') as f:

    #a list to contain the rows of the puzzle currently being read
    currentSudokuPuzzle = []
    labelCounter = 1    #each sudoku is headed y a line "Grid XY"
    for line in f.readlines()[1:]:  #throw away the first line because it's just a puzzle label

        if labelCounter % 10 == 0:
            #skip appending this line - we've hit a puzzle label header.

            #we should also reset the puzzle's row list
            sudokus.append(suPuzzle(currentSudokuPuzzle))
            currentSudokuPuzzle = []

        else:
            currentSudokuPuzzle.append([suNode(x) for x in line.rstrip('\n')])

        labelCounter += 1

    #the mod-math doesn't append the list created last.
    #TODO: come up with a cleaner way to get all of them while still label-skipping
    sudokus.append(suPuzzle(currentSudokuPuzzle))


numSolved = 0
numPuzzles = len(sudokus)

for puzzle in sudokus:
    stillChanging = True
    checkCount = 0

    while stillChanging or checkCount < 100:
        changed = 0

        #sweep check for cells with only one remaining possibility
        for r in range(suPuzzle.BOARD_SIZE):
            for c in range(suPuzzle.BOARD_SIZE):
                if puzzle.rows[r][c].numPossibilities() == 1:
                    changed += 1
                    puzzle.rows[r][c].value = puzzle.rows[r][c].possibilities[0]
                    puzzle.rows[r][c].possibilities.remove(puzzle.rows[r][c].value)

                    puzzle.updatePossibilities()


        #work across all possible values [1..9]
        for v in range(suPuzzle.BOARD_SIZE+1):

            #for each perspective, check to see if only one cell can take on a certain value
            for perspective in [puzzle.rows, puzzle.cols, puzzle.squs]:

                #loop across primary index for the current perspective
                for x in range(suPuzzle.BOARD_SIZE):

                    #if there is only one cell in this group hat can take on value i, then i should be placed there.
                    if sum([cell.possibilities.count(v) for cell in perspective[x]]) == 1:

                        #find the place where v can go
                        for y in range(suPuzzle.BOARD_SIZE):
                            if v in perspective[x][y].possibilities:
                                #change the value of this cell, and remove its possibilities.
                                #it was the only cell of this row that could have i as a value, but there could still be
                                #   changes to the column and square possibilities trackers.
                                perspective[x][y].value = v
                                perspective[x][y].possibilities = []

                        changed += 1
                        puzzle.updatePossibilities()


        checkCount += 1

        if changed == 0:
            stillChanging = False

        #puzzle.updatePossibilities()


    if puzzle.isComplete():
        numSolved += 1
    else:
        print(puzzle)
        print()

print("Solved %s sudokus, out of a total of %s" % (numSolved, numPuzzles))
