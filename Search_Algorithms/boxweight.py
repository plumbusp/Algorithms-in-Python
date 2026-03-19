# Task can't be done using Greedy.
# def min_count(weights, max_weight):
#     boxCount = 0
#     unpacked = sorted(weights, reverse=True)
#     targetLength = len(unpacked)
#     packed = []
#     currentBox = 0

#     while len(packed) != targetLength:
#         toRemove = []
#         for w in unpacked:
#             if boxCount == 0:
#                 boxCount = 1
#             if w <= max_weight:
#                 if currentBox+w > max_weight:
#                     currentBox = w
#                     boxCount += 1
#                 else:
#                     currentBox+=w
#                 toRemove.append(w)
#                 packed.append(w)
#             else:
#                 return -1
#         for i in toRemove:
#             unpacked.remove(i)
        
#     return boxCount

import itertools
import math

def min_count(weights, max_weight):
    boxCount = math.inf
    permutations = itertools.permutations(weights, len(weights))
    for perm in permutations:
        localBoxCount = 0
        currentBox = 0
        for w in list(perm):
            if w > max_weight:
                return -1
            if localBoxCount == 0:
                localBoxCount = 1
            if currentBox + w > max_weight:
                localBoxCount+=1
                currentBox = w
            else:
                currentBox+= w
        boxCount = min(boxCount, localBoxCount)
    return boxCount
            


if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3