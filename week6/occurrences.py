#Review
class OccurrenceTracker:
    def __init__(self):
        self.occurences = {}
        self.frequenceCounter = {}
        self.waysToOccur = 0

    def append(self, number):
        oldValue = self.occurences.setdefault(number, 0)
        self.occurences[number]+= 1
        newValue = self.occurences[number]

        if oldValue> 0:
            self.frequenceCounter[oldValue]-= 1
            if self.frequenceCounter[oldValue] <= 0:
                self.waysToOccur-= 1

        self.frequenceCounter[newValue]= self.frequenceCounter.get(newValue, 0)+1
        if self.frequenceCounter[newValue] == 1:
            self.waysToOccur+= 1

    def count(self):
        return self.waysToOccur

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3
    
    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901
