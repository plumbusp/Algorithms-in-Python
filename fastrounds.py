# Counts the number of rounds (passes) needed to collect numbers
# in increasing order (1..n) by scanning the list from left to right.
# Time complexity: O(n)

def count_rounds(numbers):
    seen = set()
    loopCount = 1

    previous_number = 0
    for number in numbers:
        if number == previous_number + 1:
            previous_number = number
            continue
        elif number-1 in seen:
                seen.add(number)
                continue
        else:
            seen.add(number)
            loopCount += 1
    return loopCount


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000