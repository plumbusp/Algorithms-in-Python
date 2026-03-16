import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer: Comparer):
    def customRecursiveSort(indexes):
            if len(indexes) <= 1:
                return indexes
            n = len(indexes)
            left_numbers = customRecursiveSort(indexes[:n//2])
            right_numbers = customRecursiveSort(indexes[n//2:])
            sortedIndexes = []
            leftPos= 0
            rightPos = 0
            while len(sortedIndexes) < n:
                if leftPos == len(left_numbers):
                    right_number = right_numbers[rightPos]
                    sortedIndexes.append(right_number)
                    rightPos+=1
                elif rightPos == len(right_numbers):
                    left_number = left_numbers[leftPos]
                    sortedIndexes.append(left_number)
                    leftPos+=1
                else:
                    left_number = left_numbers[leftPos]
                    right_number = right_numbers[rightPos]
                    if comparer.smaller(left_number, right_number):
                        sortedIndexes.append(left_number)
                        leftPos+=1
                    else:
                        sortedIndexes.append(right_number)
                        rightPos+=1

            return sortedIndexes

    numbers = list(range(comparer.list_size()))
    sortedIndices = customRecursiveSort(numbers)

    result = [0]*comparer.list_size()
    for i, positionIndex in enumerate(sortedIndices):
        result[positionIndex] = i + 1
    return result

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]