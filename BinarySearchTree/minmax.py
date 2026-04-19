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

    def min(self):
        currentNode = self.root
        if currentNode == None:
            return None
        while True:
            if currentNode.left == None:
                return currentNode.value
            currentNode = currentNode.left

    def max(self):
        currentNode = self.root
        if currentNode == None:
            return None
        while True:
            if currentNode.right == None:
                return currentNode.value
            currentNode = currentNode.right

if __name__ == "__main__":
    numbers = TreeSet()

    print(numbers.min()) # None
    print(numbers.max()) # None

    numbers.add(3)
    print(numbers.min()) # 3
    print(numbers.max()) # 3

    numbers.add(4)
    print(numbers.min()) # 3
    print(numbers.max()) # 4

    numbers.add(1)
    print(numbers.min()) # 1
    print(numbers.max()) # 4
