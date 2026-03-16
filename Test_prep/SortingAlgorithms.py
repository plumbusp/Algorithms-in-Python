# Logic: 1) take a list, recursivly split it
# 2) If list's length is 1, it is already sorted
# 3) add sorted lists together, sort them
def merge_sort(numbers):
    length = len(numbers)
    if length == 1:
        return numbers
    leftPart = numbers[length//2:]
    rightPart = numbers[:length//2]
    print(str(leftPart) + " Left part")
    print(str(rightPart) + " Right part")
    sortedLeft = merge_sort(leftPart)
    sortedRight = merge_sort(rightPart)

    newList = []
    j = 0
    i = 0
    while i < len(sortedRight) and j < len(sortedLeft):
        if sortedRight[i] > sortedLeft[j]:
            newList.append(sortedLeft[j])
            j+=1
        else:
            newList.append(sortedRight[i])
            i += 1
    newList.extend(sortedLeft[j:])
    newList.extend(sortedRight[i:]) 
    # be careful which pointers you use where
    # Adding leftover
    return newList

print(merge_sort([1,4,5,2,3]))