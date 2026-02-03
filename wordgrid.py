# Counts how many times a given word appears horizontally in a square grid, matching letters from left to right.

class WordFinder:
    def __init__(self):
        self.grid = []
        self.entriesSet =  set()

    def set_grid(self, grid: list):
        self.grid = grid.copy()

    def count(self,word):
        self.__searchHorizontal(word)
        print(self.entriesSet)

    def __searchHorizontal(self, word):
        for i in range(0, len(self.grid)): #rows
            entry = ""
            entry += self.grid[i][0] # i row, first column
            for j in range(1,len(self.grid[0])): #rows
                entry+= self.grid[i][j] # i row, j column
                if word in entry:
                    self.entriesSet.add((i+1,j+1)) # new entry on row i, column j (considering offset ny one)
                    entry = "" # to avoid multiple calculation of the same word

    def __searchVertically(self, word):
        for i in range(0, len(self.grid[0])): #columns
            entry = ""
            entry += self.grid[0][i] # first row, i column
            for j in range(1,len(self.grid)): #rows
                entry+= self.grid[j][i] # j row, i column
                if word in entry:
                    print(entry)
                    self.entriesSet.add((j+1,i+1)) # new entry on row j, column i (considering offset ny one)
                    entry = "" # to avoid multiple calculation of the same word
    def __searchDiagonaly(self, startUp = True):
        rows = len(self.grid) #rows
        columns = len(self.grid[0]) #columns
        for d in range(0, rows + columns-1): # for each diagonal there is
            if d % 2 == 0:
                r = min(d, rows-1) # diagonal row index is diagonal index if it is less then row amount, otherwise row amount
                c = d - rows
                # to do



if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    # print(finder.count("TA")) # 13
    # print(finder.count("RITARI")) # 3
    # print(finder.count("A")) # 8
    # print(finder.count("AA")) # 6
    # print(finder.count("RAITA")) # 0 
