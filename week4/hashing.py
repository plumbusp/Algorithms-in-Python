from string import ascii_lowercase
def hash_value(string):
    A = 23
    M = 2**32
    letterNumbers = {}
    number = 0
    for l in ascii_lowercase:
        letterNumbers[l]=number
        number+=1

    hash_value = 0
    powerIndex = len(string)-1
    for s in string:
        hash_value += letterNumbers[s]*(A**powerIndex)
        powerIndex-=1
    return hash_value % 2**32

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440