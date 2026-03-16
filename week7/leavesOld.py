#Task: Count how many leaves a tree has
# We have a function to which we give a root node. Function counts amount of leaves.

#Starting with creating Node class
class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __str__(self) -> str:
        return self.value
    
#then function
#using recursion go level down each time,
#if no children -> leaf -> add to count
# for each node looping children and looking for leafes
def count_leaves(node) -> int:
    count = 0
    if node.children == []:
        return 1
    for childNode in node.children:
        count += count_leaves(childNode)
    return count

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_leaves(tree1)) # 4