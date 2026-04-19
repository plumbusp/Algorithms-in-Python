class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        depth = 0
        if not self.root:
            self.root = Node(value)
            self.max_depth = max(depth, self.max_depth)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                depth += 1
                self.max_depth = max(depth, self.max_depth)
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                depth += 1
                self.max_depth = max(depth, self.max_depth)
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right
                
    def remove(self, value):
        node, parent = self.find_node_and_parent(value)

        if not node:
            return

        if node.left and node.right:
            next_value = self.next(value)
            self.remove(next_value)
            node.value = next_value
            return

        new_child = None
        if node.left:
            new_child = node.left
        elif node.right:
            new_child = node.right

        if not parent:
            self.root = new_child
        elif parent.left == node:
            parent.left = new_child
        else:
            parent.right = new_child

    def find_node_and_parent(self, value):
        node = self.root
        parent = None
        while node:
            if node.value == value:
                return node, parent
            parent = node
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return None, None

    def next(self, value):
        node = self.root

        result = None
        while node:
            if node.value > value:
                if not result or node.value < result:
                    result = node.value
                node = node.left
            else:
                node = node.right

        return result
    

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.add(2)
    numbers.add(5)
    numbers.add(7)
    print(numbers) # [2, 3, 5, 7]
    
    numbers.remove(3)
    print(numbers) # [2, 5, 7]

    numbers.remove(7)
    print(numbers) # [2, 5]

    numbers.remove(2)
    print(numbers) # [5]

    numbers.remove(5)
    print(numbers) # []

    numbers2 = TreeSet()
    numbers2.add(3)
    numbers2.add(4)
    print(numbers2)
    numbers2.remove(3)
    print(numbers2)