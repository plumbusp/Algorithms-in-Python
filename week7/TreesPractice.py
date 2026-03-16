class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __repr__(self):
        return str(self.value)
    
node3 = Node(0,[1,9])
node2= Node(3,[4,5])
node1 = Node(2,[node2,node3])

tree = Node(0, [
        Node(1, [
            Node(2), Node(3, [
                Node(4),Node(5)
                ])
            ])
    ])
if False:
    for node in tree.children:
        print(node.value) #1
# But how we loop through every child?
# Recursion!

def recursiveLoop(node):
    print(node.value)
    if node.children == []:
        return
    for childNode in node.children:
        recursiveLoop(childNode) 

recursiveLoop(tree) # Good. Let's add indents
# Let's track a variable across recursion. Dpeth

print("\n")

def recursiveLoopIndents(node, depth):
    print(depth*" ",node.value)
    if node.children == []:
        return
    for childNode in node.children:
        recursiveLoopIndents(childNode, depth+1) 


recursiveLoopIndents(tree,depth=0) #by rules, depth(height) counting strats at 0

