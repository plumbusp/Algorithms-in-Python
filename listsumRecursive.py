# The algorithm computes sums of all contiguous subarrays of fixed size
# Sliding window algorithm, recursive version.
# Time complexity O(n)
def find_sums(numbers, size):
    def recursiveFunction(sublistSum: int, startSublistIndex: int, sums: list):
        if startSublistIndex + size > len(numbers):
            return sums
        sublistSum = sublistSum - numbers[startSublistIndex -1] + numbers[startSublistIndex + size - 1]
        sums.append(sublistSum)
        recursiveFunction(sublistSum, startSublistIndex + 1, sums)
    
    sums = []
    sublist = numbers[0:size]
    sublistSum = sum(sublist)
    sums.append(sublistSum)
    recursiveFunction(sublistSum,1, sums)
    return sums

if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]
    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    # [1,2,3]       -- 6
    #   [2,3,4]     -- 9
    #       [3,4,5] -- 12
