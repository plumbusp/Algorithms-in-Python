class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"


def find_path(node, a, b):
    pathToA = findNode(node, a)
    pathToB = findNode(node, b)

    if pathToA == None or pathToB == None:
        return None
    
    lastCommon = 0
    #common ancestor
    while len(pathToA)> 0 and len(pathToB)> 0 and pathToA[0] == pathToB[0]:
        lastCommon = pathToA[0]
        pathToA.pop(0)
        pathToB.pop(0)
    pathToA.reverse()

    return pathToA+[lastCommon]+pathToB

def findNode(node, b):
    if node.value == b:
        return [node.value]
    for childNode in node.children:
        result = findNode(childNode, b)
        if result != None:
            return [node.value]+result
        
    return None


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None