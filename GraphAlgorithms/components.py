def find_components(nodes, edges):
    graph = {node: [] for node in nodes} # storing neighbors of each node
    for edge in edges: # each connection
        graph[edge[0]].append(edge[1]) # side 1 neighbors of side 0
        graph[edge[1]].append(edge[0])
    
    def visit(node):
        if node in components:
            return
        components[node] = counter

        for next_node in graph[node]:
            visit(next_node)

    counter = 0
    components = {}
    for node in nodes:
        if node not in components:
            counter += 1
            visit(node)

    result = {}
    for node,component in components.items():
        if component not in result:
            result[component] = []
        result[component].append(node)

    final = []
    for component in sorted(result.values()):
        final.append(sorted(component))
        
    return final

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]