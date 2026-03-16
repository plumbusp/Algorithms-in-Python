class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_levels(node):
    levels = []
    collectLevels (node, 0, levels)

    for level in levels:
        level.sort()
    return levels

def collectLevels(node, depth, levels):
    if depth == len(levels):
        levels.append([])
    levels[depth].append(node.value)

    for childNode in node.children:
        collectLevels(childNode, depth+1, levels)

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]