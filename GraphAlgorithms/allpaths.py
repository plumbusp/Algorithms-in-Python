class AllPaths:
    def __init__(self, n):
        self.nodes = list(range(1,n+1))
        self.graph = {node: [] for node in self.nodes}
        self.result = {}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count(self): # count amount of paths. I utilize DFS and DP
        self.result = {}
        count = 0
        for i in self.nodes:
            count+= self.count_from(i)
        return count
            

    def count_from(self, node)-> int:
        if node in self.result:
            return self.result[node]
        
        count = 1 # itself

        for next_node in self.graph[node]:
            count += self.count_from(next_node)
        self.result[node] = count

        return count



if __name__ == "__main__":
    counter = AllPaths(4)

    counter.add_edge(1, 2)
    counter.add_edge(1, 3)
    counter.add_edge(2, 4)
    counter.add_edge(3, 4)

    print(counter.count()) # 10

    counter.add_edge(2, 3)

    print(counter.count()) # 14