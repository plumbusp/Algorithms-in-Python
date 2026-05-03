def find_sequence(numbers):
    result = {} # saving previous longest subsequence for index i
    result[0] = [numbers[0]] # sequence of 1 element
    longest_sequence = [numbers[0]]
    for i in range(1,len(numbers)):
        result[i] = [numbers[i]]
        for j in range(i):
            if numbers[j] < numbers[i]:
                new_result = result[j] + [numbers[i]]
                if len(result[i]) < len(new_result):
                    result[i] = new_result

            if len(result[i]) > len(longest_sequence):
                longest_sequence = result[i]
    return longest_sequence
        


if __name__ == "__main__":
    print(find_sequence([9]))
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]