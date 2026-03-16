class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    
    def __str__(self) -> str:
        return self.value

# make a function that returns list (from samllest to biggest) of all subtrees in the tree
#going down each time, appending count of sublists each time 

# current problem is: we need to append all counts to some common list,
# and here is solution with some common list
commonList = []
def count_subtreesOLD(node) -> int:
    count = 1
    if node.children == []:
        commonList.extend([1])
        return count
    for childNode in node.children:
        count += count_subtreesOLD(childNode)
    commonList.extend([count])
    return count


if False:
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                Node(5),
                Node(2, [Node(6)])])
    count_subtreesOLD(tree1)
    commonList.sort()
    print(commonList) # [1, 1, 1, 1, 2, 3, 7]


# But.. the task requires the count_subtrees(node) function to output LST, containing all the counts.
# Solution to this: using second "helper" function:
#   in 'main' count_subtrees(node)->list function we will just append new counts;
#   and in 'helper'  count_subtree_size(node)->int function we 
#       will count size of the given subtree and return int.
def count_subtrees(node)-> list:
    subrees = []
    count = count_subtree_size(node)  
    subrees.extend([count])
    for childeNode in node.children:
        subrees.extend(count_subtrees(childeNode))
    return sorted(subrees)


def count_subtree_size(node)-> int:
    count = 1
    if node.children == []:
        return count
    for childNode in node.children:
        count+= count_subtree_size(childNode)
    return count



if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_subtrees(tree1)) # [1, 1, 1, 1, 2, 3, 7]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_subtrees(tree2)) # [1, 2, 3, 4]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_subtrees(tree3)) # [1, 1, 1, 4]