class MaxList:
    def __init__(self):
        self.list = []
        self.maxNumber = 0

    def append(self, number):
        self.list.append(number)
        self.maxNumber = max(self.maxNumber, number)

    def max(self):
        return self.maxNumber

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8