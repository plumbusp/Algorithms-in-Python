class RepeatList:
    def __init__(self):
        self.list = []
        self.seen = set()
        self.repeated = False
        self.maxNumber = 0

    def append(self, number):
        self.list.append(number)
        if number in self.seen:
            self.repeated = True
        self.seen.add(number)
        self.maxNumber = max(self.maxNumber, number)

    def repeat(self):
        return self.repeated

if __name__ == "__main__":
    numbers = RepeatList()

    print(numbers.repeat()) # False

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.repeat()) # False

    numbers.append(2)
    print(numbers.repeat()) # True

    numbers.append(5)
    print(numbers.repeat()) # True