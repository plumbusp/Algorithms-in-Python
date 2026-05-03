class MaxSet:
    def __init__(self, n):
        self.nodes = list(range(1,n+1))
        self.representatives = {node: None for node in self.nodes}
        self.size = {node:1 for node in self.nodes}
        self.max_component = 1

    def find(self, x) -> int:
        # find the representative of node x
        while self.representatives[x]:
            x = self.representatives[x]
        return x

    def merge(self, a, b):
        repr_a = self.find(a) # int
        repr_b = self.find(b) # int
        
        if repr_a == repr_b:
            return
        
        if self.size[repr_a] > self.size[repr_b]:
            repr_a, repr_b = repr_b, repr_a

        self.representatives[repr_a] = repr_b
        self.size[repr_b] = self.size[repr_b] + self.size[repr_a]
        self.max_component = max(self.max_component,self.size[repr_b])

    def get_max(self): # size of biggest component
        return self.max_component

if __name__ == "__main__":
    max_set = MaxSet(5)
    print(max_set.get_max()) # 1

    max_set.merge(1, 2)
    max_set.merge(3, 4)
    max_set.merge(3, 5)
    print(max_set.get_max()) # 3

    max_set.merge(1, 5)
    print(max_set.get_max()) # 5

    max_set.merge(2, 3)
    print(max_set.get_max()) # 5