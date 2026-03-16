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

def find_other(string):
    A = 23
    target = hash_value(string)
    h = target
    chars = []

    # build a new string backwards
    for _ in range(8):  # 8 chars is enough
        c = h % A
        if c == 0:
            c = 1
        chars.append(chr(ord('a') + c - 1))
        h = (h - c) // A

    other = "".join(reversed(chars))

    if other == string:
        other += "a"

    return other
if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682