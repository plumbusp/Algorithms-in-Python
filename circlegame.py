# given that n people are standing in the circle and every second go away, 
# what is the sequence of withdrawals? 
# e.g. in the group 1,2,3,4,5,6 withdrawals will look like this: 2,4,6,3,1,5. 
# Algorithm efficiency: O(n^2)
def find_order(n):
    numbers = [i for i in range(1,n+1)]

    withdrawals = []
    index = 1
    # loop until no numbers left
    while True: # O(n); works until len(numbers) == 0
        lenght = len(numbers)
        if lenght == 0:
            return withdrawals
        elif lenght == 1: # the case A handles offsets by 1 on a new loop, but can't consider the possibility that there could be only one element left
            index = 0

        if index >= lenght: 
            if index - lenght == 1: # the case A
                index = 1
            else:
                index = 0
        withdrawals.append(numbers[index])
        numbers.pop(index) #O(n); each time an element is removed, all the elements move to the left, which gives them new indexes.
        index +=1



if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(4)) # [2, 4, 3, 1]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]