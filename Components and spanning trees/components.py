class Components:
    def __init__(self, n):
        self.nodes = list(range(1,n+1))
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

        

    def count(self):
        found = set()
        count = 0
        for node in self.nodes:
            n_repr = self.find_repr(node)
            if n_repr in found:
                continue
            found.add(n_repr)
            count += 1
        return count

if __name__ == "__main__":
    components = Components(5)

    components = Components(3)
    components.add_road(1, 2)
    print(components.count())
    components.add_road(3, 2)
    print(components.count())
    components.add_road(2, 3)
    print(components.count())
    components.add_road(3, 2)
    print(components.count())
    components.add_road(3, 1)
    print(components.count())
    components.add_road(1, 3)
    print(components.count())