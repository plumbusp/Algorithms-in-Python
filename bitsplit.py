# Task: create an O(n) algorythm calculates how many ways the bit sequence
#       can be split, so that there is the same amount of 0 and 1 in both parts
 
def count_splits(sequence):
    countOnIndexesFromLeft = {}  # index: True if same amount of 0,1 until this index, False otherwise
    countOnIndexesFromRight = {} # index: True if same amount of 0,1 until this index, False otherwise
    zero = "0"
    one ="1"
    #print(sequence)

    currentValue = (0,0)
    for i in range(0, len(sequence)): # stores whether 0 and 1 amount is the same from index 0 to n of the sequence
        currentValue = (currentValue[0] + 1 if sequence[i] == zero else currentValue[0],
                        currentValue[1] + 1 if sequence[i] == one else currentValue[1])
        countOnIndexesFromLeft[i] = True if currentValue[0] == currentValue[1] else False

    currentValue = (0,0)  # stores whether 0 and 1 amount is the same from index n to 0 of the sequence
    for i in range(len(sequence)-1, -1, -1):
        currentValue = (currentValue[0] + 1 if sequence[i] == zero else currentValue[0],
                        currentValue[1] + 1 if sequence[i] == one else currentValue[1])
        countOnIndexesFromRight[i] = True if currentValue[0] == currentValue[1] else False


    splitsCount = 0
    for i in range(1, len(sequence)):
        if countOnIndexesFromLeft[i-1] == True and countOnIndexesFromRight[i] == True: # cheking if amount is the same for both sides of the split
            splitsCount += 1
    return splitsCount


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    # sequence = "01"*10**5
    # print(count_splits(sequence)) # 99999