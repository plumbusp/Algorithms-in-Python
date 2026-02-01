# Counts how many times a given word appears horizontally in a square grid, matching letters from left to right.
class WordFinder:
    def __init__(self):
        self.grid = [] #
    def set_grid(self, grid: list):
        #making a matrix out of grid
        for entry in grid:
            self.grid.append(list(entry))
    # laskee annetun sanan esiintymiskerrat ruudukossa
    def count(self,word):
        return self.__searchHorizontal(word) 

    def __searchHorizontal(self, word) -> int:
        count = 0
        for i in range(0, len(self.grid)):
            if len(word) != len(self.grid):
                continue
            currentWord = ""
            for j in range(0, len(self.grid[i])):
                if j >= len(word):
                    break
                if self.grid[i][j] == word[j]:
                    currentWord+=self.grid[i][j]
                    if currentWord == word:
                        count +=1
                        break

        return count

                



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
