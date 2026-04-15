class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
            self.size += 1
        else:
            current_node = self.root
            while True:
                if current_node.value == value:
                    return
                elif current_node.value > value:
                    if not current_node.left:
                        current_node.left = Node(value)
                        self.size += 1
                        return
                    current_node = current_node.left
                elif current_node.value < value:
                    if not current_node.left:
                        current_node.left = Node(value)
                        self.size += 1
                        return
                    current_node = current_node.left

    def __len__(self):
        return self.size

if __name__ == "__main__":
    numbers = TreeSet()
    print(len(numbers)) # 0
    numbers.add(1)
    print(len(numbers)) # 1
    numbers.add(2)
    print(len(numbers)) # 2
    numbers.add(3)
    print(len(numbers)) # 3
    numbers.add(2)
    print(len(numbers)) # 3