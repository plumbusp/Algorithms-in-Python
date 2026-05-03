import heapq
class DirectedGraph:
    def __init__(self, nodes):
        self.indexes = list(range(len(nodes)))
        self.nodes = nodes
        self.graph = {i: [] for i in self.indexes}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
            
    def find_distances(self, start_index):
        distances = {}
        for i in self.indexes:
            distances[i] = float("inf")
        distances[start_index] = 0
        
        queue = []
        heapq.heappush(queue, (0, start_index))
        
        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)
                    

        return distances

def find_steps(numbers):
    # first we need to create a directed grpah and identify all edges
    # creating a directed object and adding edges, as in task
    directed_graph = DirectedGraph(numbers)
    for i in range(len(numbers)):
        if i + numbers[i] < len(numbers):
            directed_graph.add_edge(i, i + numbers[i], numbers[i])
        if i - numbers[i] > 0:
            directed_graph.add_edge(i, i - numbers[i], numbers[i])

    # next goal is to find shortest path from start_node to the end
    distances = directed_graph.find_distances(0)
    if distances[len(directed_graph.nodes)-1] == float("inf"):
        return -1
    else:
        return distances[len(directed_graph.nodes)-1]
        

    

if __name__ == "__main__":
    print(find_steps([1, 1, 1, 1])) # 3
    print(find_steps([3, 2, 1])) # -1
    print(find_steps([3, 5, 2, 2, 2, 3, 5])) # 10
    print(find_steps([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32

    numbers = []
    for i in range(10**5):
        numbers.append(1337 * i % 100 + 1)
    print(find_steps(numbers)) # 100055