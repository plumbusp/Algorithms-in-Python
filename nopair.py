# Lists are represented by numbers in an even amount, but every list contains one number in an odd amount
# Task: create an efficient algorithm to identify that odd number
def find_number(numbers):
    seen = {} # key: number, value: (amount, isEven)
    for n in numbers:
        if n not in seen:
            seen[n] = (0, True)

        currentAmount = seen[n][0]+1
        isEven = False
        if currentAmount % 2 == 0:
            isEven = True
        seen[n] = (currentAmount, isEven)
        
    for number, tuple in seen.items():
        if tuple[1] == False:
            return number

if __name__ == "__main__":
    print(find_number([1, 2, 4, 1, 4])) # 2
    print(find_number([1])) # 1
    print(find_number([1, 1, 2, 2, 2])) # 2
    print(find_number([1, 2, 3, 1, 2])) # 3
    print(find_number([1, 2, 1, 2, 1, 2, 1])) # 2

    numbers = list(range(1, 10**5+1))
    print(find_number(numbers + [0] + numbers)) # 0