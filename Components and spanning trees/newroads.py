class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.representatives = {node: None for node in self.nodes}
        self.size = {node: 1 for node in self.nodes}

    def find_repr(self, x):
        while self.representatives[x]:  # to indure representative is a number, not None
            x = self.representatives[x]
        return x

    def add_road(self, a, b):
        a_repr = self.find_repr(a)
        b_repr = self.find_repr(b)
        if a_repr == b_repr:
            return
        if self.size[a_repr] < self.size[b_repr]:
            a_repr, b_repr = b_repr, a_repr
        self.representatives[b_repr] = a_repr
        self.size[b_repr] = self.size[a_repr] + self.size[b_repr]

class NewRoads:
    def __init__(self, n):
        self.nodes = list(range(1,n+1))
        self.edges = []
        
    def add_road(self, a, b, x):
        self.edges.append((a,b,x))

    #min weight spanning tree
    def min_cost(self):
        edges = self.edges.copy()
        sorted_edges = sorted(edges, key= lambda x:x[2])

        components = Components(self.nodes)
        total_weight = 0
        edges_count = 0
        for edge in sorted_edges:
            node_a, node_b, weight = edge
            if components.find_repr(node_a) == components.find_repr(node_b):
                continue
            components.add_road(node_a,node_b)
            total_weight+= weight
            edges_count+=1

        if edges_count != len(self.nodes)-1:
            return -1
        return total_weight

            

if __name__ == "__main__":
    new_roads = NewRoads(4)

    new_roads.add_road(1, 2, 2)
    new_roads.add_road(1, 3, 5)
    print(new_roads.min_cost()) # -1

    new_roads.add_road(3, 4, 4)
    print(new_roads.min_cost()) # 11

    new_roads.add_road(2, 3, 1)
    print(new_roads.min_cost()) # 7