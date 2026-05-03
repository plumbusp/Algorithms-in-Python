# same logic as in findlis.py, adding new steps
# now there is no need to save subsequence itself, so we change code accrodingly (to save computation time)
def count_sequences(numbers):
    result = {} # saving previous longest subsequence lengh
    count = {} # how many sequences of the longest subsequence up to that index appear
    result[0] = 1
    count[0] = 1
    longest_seq_len = 1
    seq_count = 1
    for i in range(1,len(numbers)):
        result[i] = 1
        count[i] = 1
        for j in range(i):
            if numbers[j] < numbers[i]:
                if result[j] + 1 > result[i]:
                    result[i] = result[j] + 1
                    count[i] = count[j]
                    
                elif result[j] + 1 == result[i]:
                    count[i]+= count[j]
        if result[i]> longest_seq_len:
            longest_seq_len = result[i]
            seq_count = count[i]
        elif result[i] == longest_seq_len:
            seq_count+= count[i]

    return seq_count


if __name__ == "__main__":
    print(count_sequences([1, 2, 3])) # 1
    print(count_sequences([3, 2, 1])) # 3
    print(count_sequences([1, 1, 1, 1, 1])) # 5

    print(count_sequences([1, 8, 2, 7, 3, 6])) # 1
    print(count_sequences([1, 1, 2, 2, 3, 3])) # 8
    print(count_sequences([4, 1, 5, 6, 3, 4, 3, 8])) # 3