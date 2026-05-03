# Graph -- whole data structure
# Node -- point 
# edge -- connection (what point, to what point)
def find_degrees(nodes, edges): # how many edges each node has
    graph = {node: [] for node in nodes} # storing neighbors of each node
    for edge in edges: # each connection
        graph[edge[0]].append(edge[1]) # side 1 neighbors of side 0
        graph[edge[1]].append(edge[0])

    amountOfConnections= []
    for node in nodes:
        amountOfConnections.append(len(graph[node]))
    return sorted(amountOfConnections)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(find_degrees(nodes, edges)) # [2, 2, 3, 3, 4]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_degrees(nodes, edges)) # [0, 0, 0, 0, 0]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_degrees(nodes, edges)) # [1, 1, 1, 1, 4]