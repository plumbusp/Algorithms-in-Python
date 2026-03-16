def count_pairs(numbers):
    sortedNumbers = sorted(numbers)
    count = 0
    a = 0
    middlePoint = int(len(sortedNumbers)/2)
    b = middlePoint
    while b < len(sortedNumbers) and a != middlePoint:
        if 2*sortedNumbers[a] <= sortedNumbers[b]:
            count+= 1
            a+= 1
        b+= 1
    return count





if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176