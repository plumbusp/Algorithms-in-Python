# The algorithm computes sums of all contiguous subarrays of fixed size
# Sliding window algorithm, iterative version
# Time complexity: O(n)

def find_sums(numbers, size):
    sums = []
    currentSum = sum(numbers[0:size])
    sums.append(currentSum)
    cur = 1 # current start index
    while True: # O(n)
        if cur + size > len(numbers):
            return sums
        currentSum = currentSum - numbers[cur - 1] + numbers[cur + size -1]
        sums.append(currentSum)
        cur += 1
        


if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]
    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    # [1,2,3]       -- 6
    #   [2,3,4]     -- 9
    #       [3,4,5] -- 12
    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000