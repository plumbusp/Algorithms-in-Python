# Task: check if the graph is strongly connected
# 

class Connections:
    def __init__(self, n):
        self.nodes = list(range(1, n+1))
        self.graph = {node:[] for node in self.nodes}

    def add_link(self, a, b):
        self.graph[a].append(b)

    def check_network(self):
        # does 1 reaches every node in graph?
        self.visited = set()
        for i in range(1, len(self.nodes)+1):
            self.visited = set()
            count = self.check_if_reaches(1,i)
            if count == 0:
                return False
        # does every node reach 1?
        for j in range(1, len(self.nodes)+1):
            self.visited = set()
            count = self.check_if_reaches(j,1)
            if count == 0:
                return False
        return True
    
    def check_if_reaches(self, node, target) -> int:
        count = 0
        if node in self.visited:
            return 0
        else:
            self.visited.add(node)

        if node==target:
            return 1
        
        for next_node in self.graph[node]:
            count += self.check_if_reaches(next_node, target)
        if count == 0:
            print(f"count between {node} and {target} is 0" )
        return count


if __name__ == "__main__":
    connections = Connections(5)

    connections.add_link(1, 2)
    connections.add_link(2, 3)
    connections.add_link(1, 3)
    connections.add_link(4, 5)

    print(connections.check_network()) # False

    connections.add_link(3, 5)
    connections.add_link(1, 4)

    print(connections.check_network()) # False

    connections.add_link(5, 1)

    print(connections.check_network()) # True

    connections = Connections(2)
    connections.add_link(1, 2)
    print(connections.check_network())