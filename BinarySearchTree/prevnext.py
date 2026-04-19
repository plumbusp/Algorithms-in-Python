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
        biggest_smaller = None
        if currentNode == None:
            return biggest_smaller

        while True:
            if currentNode == None:
                return biggest_smaller
            # first left that smaller than value
            if currentNode and currentNode.value < value:
                biggest_smaller = currentNode.value
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
    def next(self, value):
        currentNode = self.root
        biggest_smaller = None
        if currentNode == None:
            return biggest_smaller

        while True:
            if currentNode == None:
                return biggest_smaller
            # first right that bigger than value
            if currentNode and currentNode.value > value:
                biggest_smaller = currentNode.value
                currentNode = currentNode.left # looking for something smaller
            else:
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
    
    numbers = TreeSet()
    numbers.add(1)
    print(numbers.prev(2))
    print(numbers.next(2))
    numbers.add(2)
    print(numbers.prev(2))
    print(numbers.next(2))
    numbers.add(2)
    print(numbers.prev(3)) #2
    print(numbers.next(1)) #2