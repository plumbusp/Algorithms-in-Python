class PermutationTracker:
    def __init__(self):
        self.list = []
        self.seen = set()
        self.hasRepetitions = False
        self.leftBound = 1
        self.righBound = 1

    def append(self, number):
        self.list.append(number)
        self.leftBound = min(self.leftBound, number)
        self.righBound = max(self.righBound, number)
        if number in self.seen:
            self.hasRepetitions = True
        else:
            self.seen.add(number)

    def check(self):
        if self.hasRepetitions:
            return False
        return len(range(self.leftBound, self.righBound+1)) == len(self.seen)

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False
    
    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000