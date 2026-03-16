import random

def count_nested(intervals):
    # a2 <= a1 AND b1 <= b2, sort for a1 to be next, check bound of b2
    # if 1 2 4 5
    count = 0
    def Key(tuple: tuple):
        return(tuple[0], -tuple[1])
    sortedIntervals = sorted(intervals, key=Key)
    maxTop = 0
    for i in sortedIntervals:
        if maxTop >= i[1]:
            count += 1
        maxTop = max(maxTop, i[1])
    return count



if __name__ == "__main__":
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999