class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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
                    node.left.parent = node
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    node.right.parent = node
                    return
                node = node.right

    def remove(self, value):
        # find where the element is
        node = self.root
        value_node = None

        while True:
            if not node:
                break
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            else:
                value_node = node
                break
        
        # no such element
        if not value_node:
            return
        # case if no children
        if not value_node.right and not value_node.left:
            if value_node.parent:
                if value_node.parent.value < value_node.value:
                    value_node.parent.right = None
                elif value_node.parent.value > value_node.value:
                    value_node.parent.left = None
            else: # root
                self.root = None
            return

        # case if one child
        if self.try_remove_node_with_one_child(value_node):
            return

        # case if two children
        next_node = self.next(value_node.value) # the smallest bigger value
        # change values:
        holder = value_node.value
        value_node.value = next_node.value
        next_node.value = holder

        # our tree structure is now broken, we need to delete the nextnode with new value
        # no children (special case, because the tree is broken)
        if not next_node.left and not next_node.right:
            if next_node.parent:
                if next_node.parent.value == value_node.value: # the parent is the new root
                    value_node.right = None
                elif next_node.parent.value < next_node.value:
                    next_node.parent.right = None
                elif next_node.parent.value > next_node.value:
                    next_node.parent.left = None
            else: # root
                self.root = None
        #one child
        if self.try_remove_node_with_one_child(next_node):
            return

    def try_remove_node_with_one_child(self, value_node)-> bool:
        # case if one child
        if value_node.right and not value_node.left:
            orphan = value_node.right
            # updating parent
            orphan.parent = value_node.parent
            if value_node.parent == None:  # node is the root:
                self.root = orphan
            elif value_node == value_node.parent.right:
                value_node.parent.right = orphan
            else:
                value_node.parent.left = orphan
                
            return True
            

        if not value_node.right and value_node.left:
            orphan = value_node.left
            orphan.parent = value_node.parent
            if value_node.parent == None: # node is the root
                self.root = orphan
            elif value_node == value_node.parent.right:
                value_node.parent.right = orphan
            else:
                value_node.parent.left = orphan
            return True
        
        return False


    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)
    
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
                biggest_smaller = currentNode
                currentNode = currentNode.left # looking for something smaller
            else:
                currentNode = currentNode.right


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

    print(" ")
    numbers = TreeSet()
    numbers.add(2)
    numbers.remove(1)
    print(numbers)
    numbers.add(1)
    numbers.remove(2)
    print(numbers)

    print(" ")
    numbers = TreeSet()
    numbers.add(2)
    print(numbers)
    numbers.add(1)
    print(numbers)
    numbers.add(4)
    print(numbers)
    numbers.add(2)
    numbers.remove(2)
    print(numbers)
    # ['[2]', '[1, 2]', '[1, 2, 4]', '[1, 4]']

    numbers = TreeSet()
    numbers.add(4)
    numbers.remove(2)
    print(numbers)
    numbers.add(1)
    print(numbers)
    numbers.add(1)
    numbers.remove(4)
    print(numbers)
    numbers.add(4)
    numbers.remove(1)
    print(numbers)
    # ['[4]', '[1, 4]', '[1]', '[4]']