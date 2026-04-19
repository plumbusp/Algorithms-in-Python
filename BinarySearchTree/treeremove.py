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
        value_node_parent = None

        while True:
            if not node:
                break
            if node.value > value:
                value_node_parent = node
                node = node.left
            elif node.value < value:
                value_node_parent = node
                node = node.right
            else:
                value_node = node
                break
        
        # no such element
        if not value_node:
            return
        # case if no children
        if not value_node.right and not value_node.left:
            if value_node_parent:
                if value_node_parent.value < value_node.value:
                    value_node_parent.right = None
                elif value_node_parent.value > value_node.value:
                    value_node_parent.left = None
            else: # root
                self.root = None
            return

        # case if one child
        if self.try_remove_node_with_one_child(value_node, value_node_parent):
            return

        # case if two children
        next_node, next_node_parent = self.next(value_node.value)
        print(next_node.parent.value)
        print(f"Next node is ", next_node)
        print(f"ANd it's parent is ", next_node_parent)

        node_holder = value_node # change places of values
        value_node.value = next_node.value
        next_node.value = node_holder.value
        print(f"Now next node is: {next_node.value} and value node is {value_node.value}")
        # now we removing from that "next value", that is the current value, cause we switched their places
        if not self.try_remove_node_with_one_child(next_node, next_node_parent): # case if has a child
            if value_node_parent: # case if no children
                if value_node_parent.value < value_node.value:
                    value_node_parent.right = None
                elif value_node_parent.value > value_node.value:
                    value_node_parent.left = None
            else: # root
                self.root = None
            return


    def try_remove_node_with_one_child(self, value_node, value_node_parent)-> bool:
        # case if one child
        if value_node.right and not value_node.left:
            orphan = value_node.right
            if value_node_parent == None:  # node is the root:
                self.root = orphan
            elif value_node == value_node_parent.right:
                value_node_parent.right = orphan
            elif value_node == value_node_parent.left:
                value_node_parent.left = orphan
                
            return True
            

        if not value_node.right and value_node.left:
            orphan = value_node.left
            if value_node == value_node_parent.right:
                value_node_parent.right = orphan
            elif value_node == value_node_parent.left:
                value_node_parent.left = orphan
            else: # node is the root
                self.root = orphan
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
        currentNode_parent = None
        currentNode = self.root
        biggest_smaller = None
        if currentNode == None:
            return biggest_smaller, currentNode_parent

        while True:
            if currentNode == None:
                return biggest_smaller, currentNode_parent
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