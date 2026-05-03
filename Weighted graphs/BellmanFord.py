
import time
import random
class BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        num_rounds = len(self.nodes) - 1
        for _ in range(num_rounds):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    
        return distances
    
bellman_ford = BellmanFord([n for n in range(1,5001)])
for a in bellman_ford.nodes:
    for b in bellman_ford.nodes:
        if a < b and b-a < 10:
            bellman_ford.add_edge(a,b, random.randint(1,1000))

random.shuffle(bellman_ford.edges)

start_time = time.time()
bellman_ford.find_distances(1)
end_time =  time.time()
print("Time", end_time-start_time)