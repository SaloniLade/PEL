import heapq

def best_first_search(graph, heuristic, start, goal):

    visited = set()
    queue = []
    heapq.heappush(queue, (heuristic[start], start))
    while queue:
        h, current = heapq.heappop(queue)

        if current in visited:
            continue
        print("Visiting:", current)
        visited.add(current)

        if current == goal:
            print("Goal reached!")
            return
        for neighbour in graph[current]:
            if neighbour not in visited:
                heapq.heappush(
                    queue,
                    (heuristic[neighbour], neighbour)
                )
    print("Goal not found!")
graph = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E', 'F'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'G'],
    'H': [],
    'I': [],
    'G': []
}
heuristic = {
    'A': 15,
    'B': 13,
    'C': 10,
    'D': 14,
    'E': 11,
    'F': 8,
    'H': 9,
    'I': 4,
    'G': 0
}
best_first_search(graph, heuristic, 'A', 'G')