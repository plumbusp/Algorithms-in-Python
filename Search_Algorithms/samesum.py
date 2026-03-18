#Task: For example, [1,2,3,4] can be split into [1,4] and [2,3], both summing to 5. 
#   However, [1,2,3,5] cannot be split into two groups with equal sums.
#   Implement a function check_sum in samesum.py that returns True if such a division is possible, and False otherwise.

# Using brute force again, but optimizing it by using sliding window
import itertools
def check_sum(numbers):
    total_sum = sum(numbers)
    length =  len(numbers)
    combinations = itertools.permutations(numbers,length)

    seen = set()
    for cmb in combinations:
        choice_sum = 0
        for i in range(0, length):
            choice_sum+= cmb[i]
            if total_sum - choice_sum == choice_sum:
                return True
    return False

# The algorythm is too slow with bigger lists

# def check_sum(numbers):
#     length =  len(numbers)
#     combinations = itertools.permutations(numbers,length)

#     seen = set()
#     for cmb in combinations:
#         for i in range(0, length):
#             if sum(cmb[:i]) == sum(cmb[i:]):
#                 return True
#     return False

if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False