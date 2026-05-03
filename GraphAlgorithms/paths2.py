class CountPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def count_from(self, node):
        if node in self.result:
            return self.result[node]

        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)

        self.result[node] = path_count
        return path_count

    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)
# Plan:
# 1. create nodes to use, on each level 10 nodes, each level has some number of nodes leading to each node on the current level.
# 2. add paths to number 100 until getting the right number of paths. 
# On level 0: 10 nodes, 0 leads to them, on level 1: 10 nodes, 10 leads to each. etc.
def create_edges(x):
    edges = []
    old_x = 0
    if x == 1000000000:
        old_x = x
        x = 999999999

    number_of_digits = len(str(x))
    node = 2
    previous_nodes = [] # listS of next 10 nodes

    for level in range(number_of_digits):
        curent_ten_nodes = list(range(node, node + 10)) # len 10, but nodes are 2 - 12, 12- 22 etc.
        node += 10
        previous_nodes.append(curent_ten_nodes)
        
        # creating 10 starters
        if level == 0:
            for nd in curent_ten_nodes:
                edges.append((1, nd))
        else: # incresing amount of nodes leading to this set of current nodes each time 10x
            for nd in curent_ten_nodes:
                for pr_nd in previous_nodes[level - 1]:
                    edges.append((pr_nd, nd))
    # Now I add edges to the 10^level base based on needed zeroes
    for index, digit in enumerate(str(x)):
        digit = int(digit)
        level_needed = number_of_digits - index -1
        for i in range(digit): # digit max 9
            edges.append((previous_nodes[level_needed][i], 100))
    if old_x == 1000000000:
        #print("little change")
        edges.append((1,100))
    return edges

if __name__ == "__main__":
    edges = create_edges(1000000000)

    counter = CountPaths(range(1, 100 + 1))
    for edge in edges:
        counter.add_edge(edge[0], edge[1])
    print(counter.count_paths(1, 100))

    edges = create_edges(123456789)

    counter = CountPaths(range(1, 100 + 1))
    for edge in edges:
        counter.add_edge(edge[0], edge[1])
    print(counter.count_paths(1, 100)) # 123456789
