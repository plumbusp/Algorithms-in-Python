import itertools
import math
def find_route(distances):
    shortestRouteLength = math.inf
    shortestRoute = []
    permutations = itertools.permutations(range(2,len(distances)+1), len(distances)-1)
    for perm in permutations:
        full_route = [1] + list(perm) + [1]
        totalRoute = 0
        for i in range(1, len(full_route)):
            totalRoute += route_between(int(full_route[i-1]),int(full_route[i]), distances)
        if shortestRouteLength > totalRoute:
            shortestRouteLength = totalRoute
            shortestRoute = full_route
    return shortestRouteLength, shortestRoute

    

def route_between(first:int, second:int, distances)-> int:
    return distances[second-1][first-1]

if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]