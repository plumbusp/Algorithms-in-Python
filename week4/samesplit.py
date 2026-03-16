# How many ways a list can be split, so that there are the same numbers in each part
def count_splits(numbers):
    appeard = {}
    count = 0
    for n in numbers:
        appeard[n] = appeard.get(n,0)+1
    target = len(appeard)

    leftNumbers = {}
    rightNumbers = appeard
    # from left to right
    for i in range(len(numbers)):
        leftNumbers[numbers[i]] = leftNumbers.get(numbers[i], 0)+1
       
        rightNumbers[numbers[i]]-=1
        if rightNumbers[numbers[i]] == 0:
            rightNumbers.pop(numbers[i])
        if len(leftNumbers) == len(rightNumbers) == target:
            count += 1

    return count


            


if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1