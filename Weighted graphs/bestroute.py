class BestRoute:
    def __init__(self, n):
        self.nodes = list(range(1,n+1))
        self.edges = []

    def add_road(self, a, b, x): # add edge
        self.edges.append((a,b,x)) # next node and weight
        self.edges.append((b,a,x))

    def find_route(self, a, b): # Bellman-Ford modifide a bit
        self.distances = {}
        for node in self.nodes:
            self.distances[node] = float("inf")
        self.distances[a] = 0

        self.previous = {}
        self.previous[a] = None

        for _ in range(len(self.nodes)-1):
            for edge in self.edges:
                node_a, node_b, w = edge
                new_dist = self.distances[node_a] + w
                if new_dist < self.distances[node_b]:
                    self.distances[node_b] = new_dist
                    self.previous[node_b] = node_a

        if self.distances[b] == float("inf"):
            return -1
        else:
            return self.distances[b]
        

        
        # path = []
        # node = b
        # while node:
        #     path.append(node)
        #     if node not in self.previous:
        #         return -1
        #     node = self.previous[node]
            
        # return path




if __name__ == "__main__":
    routes = BestRoute(3)

    routes.add_road(1, 2, 2)
    print(routes.find_route(1, 3)) # -1

    routes.add_road(3, 1, 5)
    print(routes.find_route(1, 3)) # 5

    routes.add_road(2, 3, 1)
    print(routes.find_route(1, 3)) # 3