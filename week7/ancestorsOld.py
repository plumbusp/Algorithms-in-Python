class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __str__(self) -> str:
        return self.value
    

#Task: Check, if node 'a' is a parent of node 'b'. return True/False
# Solution: As we are given numerical values, 

def ancestor(node, a, b)-> bool:
    if node.value == a:
        return search_for_b_node(node,b)
    for childNode in node.children:
        result = ancestor(childNode,a,b)
        if result: # catching needed result
            return search_for_b_node(childNode,b)
    return False


def search_for_b_node(node,b)->bool:
    if node.value == b:
        return True
    for childNode in node.children:
        result = search_for_b_node(childNode,b)
        if result:
            return result
    return False

    
#Attempts: I was trying to solve this problem by looking at the depth of the node. 
# First of all, I was looking ONLY on depth, 
# but 'a' node that lower on depth doesn't mean it is PARENT of 'b'!
# Also connecting that type of functions together (is 'a' a parent of 'b' and what are their depths)
# seemed not reasonably complicated. I choosed to go with the typical way to search for value 
# in recursion:
# 1st check if value is desirable 
# 2nd check if it desirable for children, try to catch value 
# 3rd otherwise return False


# searching for depth of the value

# def find_depth(node, value, currentDepth)-> int:
#     if node.value == value:
#         return currentDepth
    
#     for childNode in node.children:
#         foundValue = find_depth(childNode, value, currentDepth+1)
#         if foundValue != -1:
#             return foundValue
#     return -1

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(ancestor(tree1, 1, 3)) # True
    print(ancestor(tree1, 2, 6)) # True
    print(ancestor(tree1, 3, 1)) # False
    print(ancestor(tree1, 5, 6)) # False
    print(ancestor(tree1, 3, 3)) # True

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(ancestor(tree2, 1, 4)) # True
    print(ancestor(tree2, 3, 2)) # False

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(ancestor(tree3, 1, 2)) # True
    print(ancestor(tree3, 1, 1)) # True
    print(ancestor(tree3, 2, 1)) # False
    print(ancestor(tree3, 5, 5)) # False