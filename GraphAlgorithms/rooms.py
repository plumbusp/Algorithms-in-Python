def explore(grid, y, x):
    if grid[y][x] != ".":
        return

    grid[y][x] = "#"

    explore(grid, y - 1, x)
    explore(grid, y + 1, x)
    explore(grid, y, x - 1)
    explore(grid, y, x + 1)


def count_rooms(grid):
    rooms= 0
    newGrid = [list(row) for row in grid]
    for y in range(len(newGrid)):
        for x in range(len(newGrid[y])):
            if newGrid[y][x] == '.':
                rooms+= 1
                explore(newGrid, y, x)
    return rooms

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2