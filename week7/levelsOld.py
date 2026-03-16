class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __str__(self) -> str:
        return self.value
    
#Task: create a function that takes the tree and return
#   list of lists, that contain numerical values of nodes from each level

# Solution: again, using 'helper' function to work with given list and append newly found
#   numerical value of levels.
#   each element in 'levels' list is [] list. depth -> index of this element.
#   so element of root goes into index = 0, second layer children into index = 1
#   How do we track depth? Increase it each time we recurse.

def find_levels(node)->list: # not recursive
    levels = []
    levels = find_level_numerical_values(node,0,levels)
    for l in levels:
        l.sort()
    return levels

def find_level_numerical_values(node, currentDepth, levels:list)->list: #shares common link for the 'levels' list
    if currentDepth == len(levels):
        levels.append([])
    levels[currentDepth].append(node.value)

    for childNode in node.children:
        if currentDepth+1 == len(levels):
            levels.append([])
        find_level_numerical_values(childNode, currentDepth+1, levels)
    return levels

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]