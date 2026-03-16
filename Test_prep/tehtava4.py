# Task: create funciton to tell what is the least number of elements to
#   remove from it to get the same numbers at the beginning and at the end.
import math

def min_removals(numbers):
    occurences = {} # number : first index to occur
    result = math.inf
    length = len(numbers)
    for i in range(0,length):
        if numbers[i] not in occurences:
            occurences[numbers[i]] = i
        if i == occurences[numbers[i]]:
            continue
        result = min(length - ((i-(occurences[numbers[i]])) + 1), result)
    return result

print(min_removals([1,2,3,4,3,6]), "expected 3")
# already correct (same start and end)
print(min_removals([1,2,3,1]), "expected 0")
# remove from end
print(min_removals([1,2,3,4,1,5]), "expected 1")
# remove from start
print(min_removals([5,1,2,3,1]), "expected 1")
# two elements same
print(min_removals([7,7]), "expected 0")
    