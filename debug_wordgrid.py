from wordgrid import WordFinder

grid = ["TIRATIRA",
        "IRATIRAT",
        "RATIRATI",
        "ATIRATIR"]

finder = WordFinder()
finder.set_grid(grid)

# Debug horizontal right-to-left for "TA"
word = "TA"
overlap = max(1, len(word)-1)

print(f"Searching for '{word}' (overlap={overlap}) right-to-left in row 1: '{grid[0]}'")
print("Column indices (0-based): ", list(range(len(grid[0]))))
print("Characters:              ", list(grid[0]))
print()

i = 0
entry = ""
for j in range(len(grid[0])-1,-1,-1):
    entry += grid[i][j]
    ends = entry.endswith(word)
    print(f"  j={j}: entry='{entry}' (len={len(entry)}), endswith('{word}')={ends}", end="")
    if ends:
        print(f" -> store ({i+1},{j+1}), entry='{entry[-overlap:]}'")
        entry = entry[-overlap:]
    else:
        print()

# Expected occurrences of "TA":
print("\nRow 1 characters at each position (1-indexed):")
for j in range(len(grid[0])):
    print(f"  ({1},{j+1}): {grid[0][j]}")
