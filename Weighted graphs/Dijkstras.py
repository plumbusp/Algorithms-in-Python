import heapq
import time
import random
class Dijkstra:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        queue = []
        heapq.heappush(queue, (0, start_node))
        
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
    

dijkstra = Dijkstra([n for n in range(1,5001)])

for a in dijkstra.nodes:
    for b in dijkstra.nodes:
        if a < b and b-a < 10:
            dijkstra.add_edge(a,b, random.randint(1,1000))

for node, neighbors in dijkstra.graph.items():
    random.shuffle(neighbors)

start_time = time.time()
dijkstra.find_distances(1)
end_time =  time.time()
print("Time", end_time-start_time)