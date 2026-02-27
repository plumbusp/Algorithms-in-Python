# O(n) algorythm that looks for a different value from the list of length > 3
def find_number(numbers):
    firstNumber = numbers[0]
    secondNumber = numbers[1]
    thirdNumber = numbers[2]

    if firstNumber == secondNumber == thirdNumber:
        pass
    elif firstNumber == secondNumber:
        return thirdNumber
    elif secondNumber == thirdNumber:
        return firstNumber
    elif firstNumber == thirdNumber:
        return secondNumber
    
    # at this stage we can be sure that all first numbers are the same
    # so I keep only the first one and gonna work only with it's value

    for i in range(2,len(numbers)):
        if numbers[i] == firstNumber:
            continue
        else:
            return numbers[i]

        

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2