# Counts how many times a given word appears horizontally in a square grid, matching letters from left to right.

class WordFinder:
    def __init__(self):
        self.grid = []
        self.entriesSet = set()

    def set_grid(self, grid: list):
        self.grid = grid.copy()

    def count(self,word) -> int:
        self.__searchHorizontal(word)
        self.__searchHorizontal(word, leftToRight=False)
        self.__searchVertically(word)
        self.__searchDiagonaly(word)
        return len(self.entriesSet)
        

    def __searchHorizontal(self, word, leftToRight=True):
        if leftToRight:
            for i in range(0, len(self.grid)): #rows
                entry = ""
                for j in range(0,len(self.grid[0])): #columns
                    entry+= self.grid[i][j] # i row, j column
                    if word in entry:
                        self.entriesSet.add((i+1,j+1, )) # new entry on row i, column j (considering offset ny one)
                        entry = "" # to avoid multiple calculation of the same word
        else:
            for i in range(0, len(self.grid)): #rows
                entry = ""
                for j in range(len(self.grid[0])-1,-1,-1): #columns
                    if entry.endswith(word):
                        self.entriesSet.add((j+1,i+1)) # new entry on row j, column i (considering offset ny one)
                        entry = "" # to avoid multiple calculation of the same word
                    entry+= self.grid[i][j] # j row, i column
    
    def __searchVertically(self, word):
        for i in range(0, len(self.grid[0])): #columns
            entry = ""
            entry += self.grid[0][i] # first row, i column
            for j in range(1,len(self.grid)): #rows
                if entry.endswith(word):
                    self.entriesSet.add((j+1,i+1))
                    entry = "" 
                entry+= self.grid[j][i]
    
    def __searchDiagonaly(self, word, fromTopLeft = True):
        diagonalResultsList = []
        rows = len(self.grid) -1 #rows (in index style)
        columns = len(self.grid[0]) -1 #columns (in index style)

        def gothroughDiagonal(self, diagonal):
            entry = ""
            if d % 2 == 0: # going UP
                r = min(d, rows) # start row index is diagonal index if it is less then row amount, otherwise row amount
                c = d - r
                while r >= 0 and c <= columns:
                    if entry.endswith(word):
                        self.entriesSet.add((r+1,c+1))
                        entry = "" 
                    entry += self.grid[r][c]
                    r -= 1
                    c += 1
            else:   # going DOWN
                c = min(d, columns) # start column index is diagonal index if it is less or equal to column amount, otherwise column amount
                r = d - c
                while r <= rows and c >= 0:
                    if entry.endswith(word):
                        self.entriesSet.add((r+1,c+1))
                        entry = "" 
                    entry += self.grid[r][c]
                    r += 1
                    c -= 1

        if fromTopLeft:
            for d in range(rows + columns-1): # for each diagonal there is
                gothroughDiagonal(self, d)
        else:
            for d in range(rows + columns-1,-1,-1): # for each diagonal there is
                gothroughDiagonal(self, d)





if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0 
