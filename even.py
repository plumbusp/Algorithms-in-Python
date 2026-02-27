# the task was to create an O(n) algorithm that would count an amount of sublists with all even numbers
import math
def count_sublists(numbers):
    evensInRow = 0
    count = 0
    for n in numbers:
        thisIsEven = (n % 2 == 0)
        if thisIsEven:
            evensInRow += 1
            count += evensInRow # 1 even number: 1 sublist, 2: 3, 3: 6, 4: 10, so each time the number of sublists grown by thenumber of current elements 
        else:
            evensInRow = 0
    return count

            


if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000
