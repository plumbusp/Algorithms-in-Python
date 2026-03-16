# Task: The key code is a sequence of 4 numbers from 1 to 9. Given string with some unknow elements
#   create a list of all the possible key codes in this string. Key codes cannot repeat existing keys or each other.
# Solution: Find indexes of unknown numbers, create permutations of those numbers using itertools,
#   use zip(iter1,iter2) to connect unknown indexes with each permutation and append new value 
#   (from combining permutations with pattern string) to the 'solutions' list.

import itertools

def find_codes(pattern):
    unknownIndexes = [i for i in range(0,len(pattern)) if pattern[i] == "?"]
    numbersForCombinations = list(range(1,10))
    for i in range(len(pattern)):
        if pattern[i] != "?":
            numbersForCombinations.remove(int(pattern[i]))

    solutions = []
    repetitions = itertools.permutations(numbersForCombinations, len(unknownIndexes)) # we need permutations in amount of unknown indexes
    for rep in repetitions:
        newStringList = list(pattern)
        for pos, value in zip(unknownIndexes, rep): # same amount of indexes in both, thanks to line 10
            newStringList[pos] = str(value)
        solutions.append("".join(newStringList))
    return solutions

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024