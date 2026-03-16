#Task: given the list, find all the steps to go from smallest number to biggest
def count_steps(numbers):
    beforeSorted = {numbers[index]:index for index in range(len(numbers))}
    sortedList = sorted(numbers)
    afterSorted = {sortedList[index]:index for index in range(len(sortedList))}
    ways = 0
    if len(sortedList) == 1:
        return 0
    previousNumber = sortedList[0]
    # finding how to get to first element
    ways+= abs(afterSorted[sortedList[0]]- beforeSorted[sortedList[0]])
    for number, _ in afterSorted.items():
        ways += abs(beforeSorted[number]-beforeSorted[previousNumber]) # step between old versions of numbers
        previousNumber = number
        
    return ways

if __name__ == "__main__":
    print(count_steps([1])) # 0
    print(count_steps([1, 2, 3])) # 2
    print(count_steps([3, 2, 1])) # 4
    print(count_steps([42, 1337, 1, 10**9])) # 7
    print(count_steps([1, 3, 5, 7, 8, 6, 4, 2])) # 28
    print(count_steps([10**6, 10**8, 10**7, 10**9])) # 5

    numbers = [(x * 999983) % 10**9 + 1 for x in range(10**5)]
    print(count_steps(numbers)) # 4871908997