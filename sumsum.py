#Task: create an O(n) algorithm  to calculate the sum of all sublists
def count_sum(numbers):
    sum = 0
    length = len(numbers)
    for i in range(0, length):
        sum += numbers[i] * (i+1) * (length-i)  # (i+1): total start points for subarrays that contain index i (!length at i)
        # (length-i): total end points for subarrays that contain index i
    return sum

if __name__ == "__main__":
    print(count_sum([1, 2, 3])) # 20
    print(count_sum([42])) # 42
    print(count_sum([1, 1, 1, 1])) # 20
    print(count_sum([2, 1, 7, 8, 5, 1, 3, 1])) # 484

    numbers = list(range(1, 10**5))
    print(count_sum(numbers)) # 8333333332500000000