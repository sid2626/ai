import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance

def best_first_search_robot(grid, start, goal):
    heap = []
    heapq.heappush(heap, (heuristic(start, goal), start))
    visited = set()
    came_from = {start: None}

    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            # reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] == 0 and
                neighbor not in visited):
                heapq.heappush(heap, (heuristic(neighbor, goal), neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current
    return None

# Example usage
grid = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [0,1,1,0]
]
start = (0,0)
goal = (3,3)
path = best_first_search_robot(grid, start, goal)
print("Path:", path)
