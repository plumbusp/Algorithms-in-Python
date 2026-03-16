class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __str__(self) -> str:
        return self.value
    
# Now let's work with depth (height)
# Function that counts how many nodes are on the certain depth

# depth parameter is the certain depth we want to count nodes on
# let's move down the tree until a certain depth
# when reached it, add to the counter
# as the depth parameter defines the certain depth, we can just decrese it by one each time we go down

def count_nodes(node, depth)-> int:
    count = 0
    if depth == 0:
        return 1
    elif depth != 0 and node.children == []: # no need for this, if there are no children, the method just won't go to another recursive round.
        return 0
    for childNode in node.children:
        count += count_nodes(childNode,depth-1)
    return count

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_nodes(tree1, 0)) # 1
    print(count_nodes(tree1, 1)) # 3
    print(count_nodes(tree1, 2)) # 3
    print(count_nodes(tree1, 3)) # 0