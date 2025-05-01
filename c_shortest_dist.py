import heapq

def best_first_search_graph(graph, start, goal, heuristic):
    heap = []
    heapq.heappush(heap, (heuristic[start], start))
    visited = set()
    came_from = {start: None}

    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(heap, (heuristic[neighbor], neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    return None

# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 4)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
# Example heuristic values for each city
heuristic = {'A': 5, 'B': 3, 'C': 4, 'D': 6, 'E': 2, 'F': 0}

start = 'A'
goal = 'F'
path = best_first_search_graph(graph, start, goal, heuristic)
print("Shortest Path:", path)
