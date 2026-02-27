# the task is to create an O(n) algorythm that will count the amount of sublists in which numbers are increasing
def count_sublists(numbers):
    previousNumber = -1
    count = 0
    increadingInRow = 0
    for n in numbers:
        if n > previousNumber:
            increadingInRow += 1
        else:
            increadingInRow = 1
        previousNumber = n
        count += increadingInRow
    return count


        
if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000