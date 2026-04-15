class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def prev(self, value):
        currentNode = self.root
        if currentNode == None:
            return None
        while True:
            if currentNode == None:
                return None
            elif currentNode.value >= value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                return currentNode.value

    def next(self, value):
        currentNode = self.root
        if currentNode == None:
            return None
        while True:
            if currentNode == None:
                return None
            elif currentNode.value > value:
                return currentNode.value
            elif currentNode.value <= value:
                currentNode = currentNode.right

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.add(2)
    numbers.add(5)
    numbers.add(7)

    print(numbers.prev(5)) # 3
    print(numbers.prev(4)) # 3
    print(numbers.prev(3)) # 2
    print(numbers.prev(2)) # None

    print(numbers.next(4)) # 5
    print(numbers.next(5)) # 7
    print(numbers.next(6)) # 7
    print(numbers.next(7)) # None