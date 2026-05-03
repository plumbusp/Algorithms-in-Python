# How to store data about a graph?
# One of the ways: store each node and neighboors of each 
#   node (or edges, which in this case the same thing).

# How do we initialize such graph? 
# Let's have set of nodes and add edges manualy.
class Graph():
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = {node:[] for node in self.nodes} # Creating adjacency list, that shows by which edges we can get into that node
    def add_edge(self, nodeA, nodeB):
        self.edges[nodeA].append(nodeB)
        self.edges[nodeB].append(nodeB)

    def __str__(self) -> str:
        string = ""
        for edge, connetions in self.edges.items():
            string += f"   Edge {edge} " + str(connetions) + "\n"
        return string
    
    ##
    def visitNeighbors(self, node):
        if node in self.visited:
            return
        self.visited.add(node)
        for neighbor in self.edges[node]:
            self.visitNeighbors(neighbor)
    # Returns all reachable nodes.
    # Uses DFS
    def graphEcosystem(self, startNode):
        self.visited = set()
        self.visitNeighbors(startNode)
        return self.visited
    ##

g = Graph([1, 2, 3, 4, 5])

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 5)
print(g.graphEcosystem(1))

