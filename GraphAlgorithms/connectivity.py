def connected(nodes, edges):
    graph = {node: [] for node in nodes} # storing neighbors of each node
    for edge in edges: # each connection
        graph[edge[0]].append(edge[1]) # side 1 neighbors of side 0
        graph[edge[1]].append(edge[0])
    
    visited = set()
    def visit(node):
        if node in visited:
            return
        visited.add(node)

        for next_node in graph[node]:
            visit(next_node)
    
    visit(nodes[0])
    return len(visited)== len(nodes)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges)) # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges)) # True