import heapq

def a_star(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()
    while queue:
        f, g, current, path = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        print("Visiting:", current, "f =", f)

        if current == goal:
            print("Goal reached!")
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return

        for neighbour, cost in graph[current]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )
    print("Goal not found!")
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 3), ('E', 2)],
    'C': [('A', 4), ('E', 1)],
    'D': [('B', 3)],
    'E': [('B', 2), ('C', 1), ('G', 3)],
    'G': [('E', 3)]
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}
a_star(graph, heuristic, 'A', 'G')