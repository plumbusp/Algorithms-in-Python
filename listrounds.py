# Collects numbers in increasing order (1..n) by scanning the list from left to right.
# Time complexity: O(n^2)

def find_rounds(numbers: list):
    if len(numbers) == 0:
        return None
    
    sorted_lists = []
    last_number = 0
    while True:
        listEntry = []
        for number in numbers:
            if last_number == len(numbers):
                return sorted_lists
            if number - last_number == 1:
                listEntry.append(number)
                last_number = number
        sorted_lists.append(listEntry)



if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
