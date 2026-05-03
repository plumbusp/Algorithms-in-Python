class GraphGame:
    def __init__(self, n):
        self.nodes = [i for i in range(1,n+1)]
        self.edges = {node:[] for node in self.nodes}
        self.conditions = {}

    def add_link(self, a, b):
        self.edges[a].append(b)

    def winning(self, x):
        result = self.check_neighbors(x)
        return result

    def check_neighbors(self, node)-> bool:
        if node in self.conditions:
            return self.conditions[node]
        for next_node in self.edges[node]:
            if self.check_neighbors(next_node) == False:
                self.conditions[node] = True
                return True # winning
        self.conditions[node] = False
        return False
        

if __name__ == "__main__":
    game = GraphGame(6)

    game.add_link(3, 4)
    game.add_link(1, 4)
    game.add_link(4, 5)

    print(game.winning(3)) # False
    print(game.winning(1)) # False

    game.add_link(3, 1)
    game.add_link(4, 6)
    game.add_link(6, 5)

    print(game.winning(3)) # True
    print(game.winning(1)) # False
    print(game.winning(2)) # False

    game = GraphGame(100)
    for a in range(1, 100 + 1):
        for b in range(a + 1, 100 + 1):
            game.add_link(a, b)
    for x in range(1, 100 + 1):
        print(game.winning(x))