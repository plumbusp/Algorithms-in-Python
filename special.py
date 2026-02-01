# Checks whether the sum of the squares of a year’s digits consists of identical digits only. 
# Returns true if all digits in that sum are the same, otherwise false.
def check_year(year):
    yearString = str(year)
    yearNumbers = [int(letter) for letter in yearString]
    numersSquareSum = sum([yearNumbers[i]**2 for i in range(0, len(yearNumbers))])
    isSpecial = True
    numersSquareSumStr = str(numersSquareSum)
    for i in range(0, len(numersSquareSumStr)):
        if i == 0:
            continue
        if numersSquareSumStr[i-1] != numersSquareSumStr[i]:
            isSpecial = False
            break
    return isSpecial


if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2000)) # True
    print(check_year(2026)) # True
    print(check_year(2029)) # False
    print(check_year(9215)) # True