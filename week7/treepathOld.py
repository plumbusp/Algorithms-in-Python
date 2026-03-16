class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __str__(self) -> str:
        return self.value
    

    
# TO_DO: FIX
# Task: find path from one to another nodes, both potentially non-root.
# Solution: since making logic of going back "up" at binary tree and then potentially
#   down to another branch would be unessesary comlex, I will use the logic that:
#   if  we found a path from root to node 'a' and path to root 'b', then path from one to 
#   another is just united paths of them both

def find_path(node, a, b):
    pathToA = fins_path_helper(node,a,[])
    pathToB = fins_path_helper(node,b,[])
    pathToA.reverse()
    pathToB.reverse()
    pathToB.pop(-1)
    path = pathToA + pathToB

    return path
    
def fins_path_helper(node, a, path)-> list:
    path.append(node.value)
    if node.value == a:
        return path
    
    result = []
    for childNode in node.children:
        result = fins_path_helper(childNode,a,path) #catching value
        if result != []:
            break

    if result == []: # no result OR leaf and not a target value -> backtracking (if no for loop happend)
        path.pop(-1)
        return []
    
    return path



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