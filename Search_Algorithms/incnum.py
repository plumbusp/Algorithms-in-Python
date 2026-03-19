# Task: Count how many raising numbers of a given length can be formed out of given numbers.
#       For example if length is 3 and numbers are "123", raising nubers will be 111, 112, 113, 122, 123, 133, 222, 223, 233 and 333.
# Solutions: Utilizing itertools.combinations_with_replacement, as it already has ascending and order doesn't matter

import itertools
def count_numbers(length, numbers):
    numbers = [int(n) for n in numbers]
    if len(numbers) == 1 and numbers[0] == 0 and length >1:
        return 0
    count = 0
    combinations = list(itertools.combinations_with_replacement(numbers, length))
    for comb in combinations:
        if comb[0] == 0 and length != 1:
            continue
        count+=1

    return count


if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758