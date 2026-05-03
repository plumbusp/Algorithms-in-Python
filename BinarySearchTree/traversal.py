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
    # O(n)
    def __repr__(self):
        items = []
        stack = []
        node = self.root
        while True:
            if not stack and not node:
                break
            # Go left as far as i can
            while node:
                stack.append(node)
                node = node.left
            # If no, check tree of next smallest item
            node = stack.pop()
            items.append(node.value)
            node = node.right
        return f"[{', '.join([str(i) for i in items])}]"

if __name__ == "__main__":
    numbers = TreeSet()
    print(numbers)

    numbers.add(4)
    numbers.add(1)
    numbers.add(2)
    numbers.add(5)
    numbers.add(8)
    numbers.add(7)

    print(numbers) # [1, 2, 4, 5, 7, 8]