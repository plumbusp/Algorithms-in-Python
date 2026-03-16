# Counts how many times a given word appears horizontally in a square grid, matching letters from left to right.

class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.coordinates = {}
        for row in range(0, len(self.grid)):
            for column in range(0, len(self.grid[row])):
                self.coordinates[(row,column)] = self.grid[row][column]
        
        self.takenCoordinates = []

    def count(self, word):
        rows = len(self.grid)
        cols = len(self.grid[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                # Horizontal RIGHT
                rowCoordinates = []
                for i, char in enumerate(word):
                    if (row, col+i) not in self.coordinates:# out of bounds
                        break
                    rowCoordinates.append((row, col+i))
                if not self.__checkIfWordExists(rowCoordinates):
                    self.takenCoordinates.extend(rowCoordinates)
                    count+= 1

                #Horizontal LEFT
                coordinates = []
                for i, char in enumerate(word):
                    if (row, col - i) not in self.coordinates or self.coordinates[(row, col - i)] != char:
                        break
                    coordinates.append((row, col - i))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

                # Vertical down
                coordinates = []
                for i, char in enumerate(word):
                    if (row + i, col) not in self.coordinates or self.coordinates[(row + i, col)] != char:
                        break
                    coordinates.append((row + i, col))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

                # Vertical up
                coordinates = []
                for i, char in enumerate(word):
                    if (row - i, col) not in self.coordinates or self.coordinates[(row - i, col)] != char:
                        break
                    coordinates.append((row - i, col))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

                # Diagonal down-right
                coordinates = []
                for i, char in enumerate(word):
                    if (row + i, col + i) not in self.coordinates or self.coordinates[(row + i, col + i)] != char:
                        break
                    coordinates.append((row + i, col + i))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

                # Diagonal down-left
                coordinates = []
                for i, char in enumerate(word):
                    if (row + i, col - i) not in self.coordinates or self.coordinates[(row + i, col - i)] != char:
                        break
                    coordinates.append((row + i, col - i))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

                # Diagonal up-right
                coordinates = []
                for i, char in enumerate(word):
                    if (row - i, col + i) not in self.coordinates or self.coordinates[(row - i, col + i)] != char:
                        break
                    coordinates.append((row - i, col + i))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

                # Diagonal up-left
                coordinates = []
                for i, char in enumerate(word):
                    if (row - i, col - i) not in self.coordinates or self.coordinates[(row - i, col - i)] != char:
                        break
                    coordinates.append((row - i, col - i))
                else:
                    if not self.__checkIfWordExists(coordinates):
                        self.takenCoordinates.extend(coordinates)
                        count += 1

            return count
        
    def __checkIfWordExists(self, wordCoordinates)-> bool:
        sortedCoordinates = sorted(wordCoordinates)
        self.takenCoordinates.sort()
        count = 0
        for c in self.takenCoordinates:
            if c in sortedCoordinates:
                count +=1
        if count >= len(sortedCoordinates):
            return True
        return False
    







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
