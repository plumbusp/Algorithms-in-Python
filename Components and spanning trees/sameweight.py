class UnionFind:
    def __init__(self, nodes):
        self.nodes = nodes
        self.representatives = {node: None for node in self.nodes}
        self.size = {node: 1 for node in self.nodes}

    def find(self, x):
        while self.representatives[x]:  # to indure representative is a number, not None
            x = self.representatives[x]
        return x

    def union(self, a, b):
        a_repr = self.find(a)
        b_repr = self.find(b)
        if a_repr == b_repr:
            return
        if self.size[a_repr] < self.size[b_repr]:
            a_repr, b_repr = b_repr, a_repr
        self.representatives[b_repr] = a_repr
        self.size[b_repr] = self.size[a_repr] + self.size[b_repr]

    



class SameWeight:
    def __init__(self, n):
        self.nodes = list(range(1,n+1))
        self.edges = []

    def add_edge(self, a, b, x):
        self.edges.append((a,b,x))

    def check(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.nodes)
        self.unused_edges = []

        i = 0
        while i < len(self.edges):
            # Collect group of edges with the same weight
            w = self.edges[i][2]
            group = []
            while i < len(self.edges) and self.edges[i][2] == w:
                group.append(self.edges[i])
                i += 1

            # Local UF to track connections made only within this weight group
            local_uf = UnionFind(self.nodes)
            for a, b, _ in group:
                if global_uf.find(a) != global_uf.find(b):
                    local_uf.union(a, b)

            # Now check each edge: cycle-forming edges must cycle within the local group
            for a, b, _ in group:
                if global_uf.find(a) != global_uf.find(b):
                    global_uf.union(a, b)
                else:
                    # Cycle — only ok if both endpoints are connected in local_uf too
                    if local_uf.find(a) != local_uf.find(b):
                        return False

        return True
    

if __name__ == "__main__":
    same_weight = SameWeight(4)

    same_weight.add_edge(1, 2, 2)
    same_weight.add_edge(1, 3, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(1, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(3, 4, 3)
    print(same_weight.check()) # True

    same_weight.add_edge(2, 4, 1)
    print(same_weight.check()) # False
    print("")
    same_weight = SameWeight(3)
    same_weight.add_edge(3, 2, 26)
    print(same_weight.check())
    same_weight.add_edge(2, 3, 57)
    print(same_weight.check())
    same_weight.add_edge(2, 1, 5)
    print(same_weight.check())
    same_weight.add_edge(2, 3, 32)
    print(same_weight.check())
    same_weight.add_edge(3, 2, 76)
    print(same_weight.check())
    same_weight.add_edge(3, 2, 57)
    print(same_weight.check())