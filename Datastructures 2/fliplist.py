import collections
class FlipList:
    def __init__(self):
        self.deque = collections.deque()
        self.flippedDeque = collections.deque()

    def __repr__(self):
        return f"[{', '.join(map(str, self.deque))}]"

    def add_first(self, x):
        self.deque.appendleft(x)
        self.flippedDeque.append(x)

    def add_last(self, x):
        self.deque.append(x)
        self.flippedDeque.appendleft(x)

    def flip(self):
        holder = self.deque
        self.deque = self.flippedDeque
        self.flippedDeque = holder

if __name__ == "__main__":
    numbers = FlipList()
    for i in range(10**5):
        numbers.add_first(2 * i)
        numbers.add_last(2 * i + 1)
        numbers.flip()
    print("ready")