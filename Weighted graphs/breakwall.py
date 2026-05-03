import heapq
class Labirynth:
    def __init__(self, plan):
        self.start_node = None
        self.end_node = None
        self.matrix = {}
        i = -1
        j = -1
        for line in plan:
            i+=1
            j=-1
            for element in line:
                j+=1
                self.matrix[(i,j)] = element
                if element == "A":
                    self.start_node = (i,j)
                elif element == "B":
                    self.end_node = (i,j)

        self.graph = {tuple: [] for tuple in self.matrix} # stores elements in format (i_1,j_1):[((i_2,j_2), weight),((i_3,j_3), weight)]
        
    def add_edge(self, tuple_a, tuple_b): # we add only possible connections
        if self.matrix[tuple_a] == "#" or self.matrix[tuple_b] == "#":
            return
        weight_char = self.matrix[tuple_b]
        weight = 1 if weight_char == "*" else 0
        self.graph[tuple_a].append((tuple_b, weight))
        
    def find_distances(self):
        distances = {}
        for tuple in self.matrix:
            distances[tuple] = float("inf")
        distances[self.start_node] = 0
        
        queue = []
        heapq.heappush(queue, (0, self.start_node))
        
        visited = set()
        while queue:
            tuple_a = heapq.heappop(queue)[1]
            if tuple_a in visited:
                continue
            visited.add(tuple_a)

            for tuple_b, weight in self.graph[tuple_a]:
                new_distance = distances[tuple_a] + weight
                if new_distance < distances[tuple_b]:
                    distances[tuple_b] = new_distance
                    new_pair = (new_distance, tuple_b)
                    heapq.heappush(queue, new_pair)
                    
        return distances
    
def find_route(grid):
    labirynth = Labirynth(grid)
    for tuple1 in labirynth.matrix:
        i, j = tuple1
        if (i - 1, j) in labirynth.matrix:
            labirynth.add_edge(tuple1, (i-1,j))
        if (i, j-1) in labirynth.matrix:
            labirynth.add_edge(tuple1, (i,j-1))
        if (i+1, j) in labirynth.matrix:
            labirynth.add_edge(tuple1, (i+1, j))
        if (i, j+1) in labirynth.matrix:
            labirynth.add_edge(tuple1, (i, j+1))

    distances = labirynth.find_distances()
    return distances[labirynth.end_node]

    # creating edges for every node. 
    # Finding shortest path from A to each node
    # Eventually finding shortest path from A to B

if __name__ == "__main__":
    grid = ["########",
            "#*A*...#",
            "#.*****#",
            "#.**.**#",
            "#.*****#",
            "#..*.B.#",
            "########"]
    print(find_route(grid)) # 2