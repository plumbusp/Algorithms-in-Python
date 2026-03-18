# Task: You are given a set of cards represented as numbers (e.g., [2,1,4,6]). 
#       Each number is a card value, and suits are irrelevant. 
#       Determine how many combinations of these cards sum to a given target.
#       For example, with [2,1,4,6] and target sum 6, there are two valid combinations: 2 + 4 and 6.

# Solution: create combinations of all lengths, from 1 to len(cards); loop through combinations,
#       check if combination sum is targetSum --- if it is, increase count of such combinations; return count

# Time:  O(2^n) - we generate all subsets
# Space: O(2^n) - storing all combinations
# Note:  not optimal for large inputs; dynamic programming would reduce to O(n * target)       
import itertools
def count_combinations(cards:list, targetSum: int):
    combinations = []
    for i in range(1, len(cards)+1):
        combinations.extend(list(itertools.combinations(cards, i)))

    targetCombinations = 0
    for comb in combinations:
        if sum(comb) == targetSum:
            targetCombinations += 1

    return targetCombinations
        

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252