# Validates a number using a checksum:
# the digits (except the last) are weighted in a repeating 3-7-1 pattern,
# summed, and the final digit must match the amount needed to reach the next multiple of ten.
# It also requires the number to start with 0.

from functools import reduce
def check_number(number: str):
    digitsList = [int(num) for num in number[0:-1]]
    if not digitsList:
        return False 
    if digitsList[0] != 0:
        return False
    factors = [3,7,1] 
    multipliedDigits = []
    for i in range(0, len(digitsList)):
        multipliedDigits.append(digitsList[i]*factors[i%3])

    tarkastusnumero = reduce(lambda sum, element: sum + element, multipliedDigits)
    if tarkastusnumero % 10 ==0:
        distance = 0
    else:
        nextTen = (tarkastusnumero + 9) // 10 * 10
        distance = nextTen - tarkastusnumero

    if int(number[-1]) != distance:
        return False
    else:
        return True

    # 3,7,1,3,7,1,3,7

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("5350961940")) # False