class DistanceTracker:
    def __init__(self):
        self.list = []
        self.distances = {} # number: (sum, time the number occured, sum of positions)
        self.currentIndex = 0

    def append(self, number):
        self.list.append(number)
        self.distances.setdefault(number,(0,0,0))
        sum, count, indexSum = self.distances[number]
        sum += self.currentIndex*count - indexSum
        indexSum+= self.currentIndex
        count += 1

        self.distances[number] = (sum, count, indexSum)
        self.currentIndex +=1


    def sum(self, number):
        try:
            if self.distances[number][1] > 1:
                return self.distances[number][0]
            return 0
        except:
            return 0

if __name__ == "__main__":
    tracker = DistanceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    tracker.append(3)
    tracker.append(1)
    tracker.append(2)
    tracker.append(1)

    print(tracker.sum(1)) # 24
    print(tracker.sum(2)) # 5
    print(tracker.sum(3)) # 1

    tracker.append(1)
    tracker.append(2)
    tracker.append(3)

    print(tracker.sum(1)) # 42
    print(tracker.sum(2)) # 16
    print(tracker.sum(3)) # 14

    tracker = DistanceTracker()
    print(tracker.sum(1)) # 0
    tracker.append(1)
    print(tracker.sum(1)) # 0

    
    tracker = DistanceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(1)
        total += tracker.sum(1)
    print(total) # 4166749999583325000