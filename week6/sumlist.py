class SumList:
    def __init__(self):
        self.sumOnIndex = {}
        self.list = []
        self.index = 0

    def append(self, number):
        self.list.append(number)
        if self.index == 0:
            self.sumOnIndex[self.index] = number
        else:
            self.sumOnIndex[self.index] = self.sumOnIndex[self.index-1] + number
        self.index+= 1

    def sum(self, a, b):
       lowerBound = self.sumOnIndex[a-1] if a>0 else 0
       return self.sumOnIndex[b]- lowerBound

if __name__ == "__main__":
    numbers = SumList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(5)

    print(numbers.sum(0, 4)) # 15
    print(numbers.sum(1, 1)) # 2
    print(numbers.sum(1, 3)) # 9
    print(numbers.sum(2, 3)) # 7
    print(numbers.sum(0, 3)) # 10

    numbers.append(1)
    print(numbers.sum(0, 5)) # 16
    print(numbers.sum(5, 5)) # 1
    
    numbers = SumList()
    total = 0
    for i in range(10**5):
        numbers.append(i + 1)
        total += numbers.sum(i // 2, i)
    print(total) # 125005000050000