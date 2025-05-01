def water_jug_dfs(capacity1, capacity2, target):
   
    stack = [(0, 0)]  # Stack for DFS with the initial state (0, 0)
    visited = set()  # Set to track visited states
    path = []  # To store the final solution path

    def dfs(state):
        
        if state in visited:
            return False

        visited.add(state)
        path.append(state)

        # Check if we've reached the target
        x, y = state
        if x == target or y == target:
            return True

        # Generate all possible moves
        possible_moves = [
            (capacity1, y),  # Fill Jug1
            (x, capacity2),  # Fill Jug2
            (0, y),          # Empty Jug1
            (x, 0),          # Empty Jug2
            (max(x - (capacity2 - y), 0), min(capacity2, x + y)),  # Pour Jug1 -> Jug2
            (min(capacity1, x + y), max(y - (capacity1 - x), 0)),  # Pour Jug2 -> Jug1
        ]

        for move in possible_moves:
            if move not in visited:
                if dfs(move):
                    return True

        # Backtrack if no solution is found from this state
        path.pop()
        return False

    if dfs((0, 0)):
        return path
    else:
        return None


def water_jug_bfs(capacity1, capacity2, target):
   
    from collections import deque

    queue = deque([(0, 0)])  # Queue for BFS with the initial state (0, 0)
    visited = set()  # Set to track visited states
    parent = {}  # To reconstruct the path

    # BFS Loop
    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        # Check if we've reached the target
        x, y = current
        if x == target or y == target:
            # Reconstruct the path from parent
            path = []
            while current is not None:
                path.append(current)
                current = parent.get(current)
            return path[::-1]  # Return the path in correct order

        # Generate all possible moves
        possible_moves = [
            (capacity1, y),  # Fill Jug1
            (x, capacity2),  # Fill Jug2
            (0, y),          # Empty Jug1
            (x, 0),          # Empty Jug2
            (max(x - (capacity2 - y), 0), min(capacity2, x + y)),  # Pour Jug1 -> Jug2
            (min(capacity1, x + y), max(y - (capacity1 - x), 0)),  # Pour Jug2 -> Jug1
        ]

        for move in possible_moves:
            if move not in visited and move not in queue:
                queue.append(move)
                parent[move] = current  # Track the parent to reconstruct the path

    return None  # If no solution is found


# Test Case
capacity1 = 4
capacity2 = 3
target = 2

print("DFS Steps:")
dfs_steps = water_jug_dfs(capacity1, capacity2, target)
print(dfs_steps if dfs_steps else "No solution found")

print("\nBFS Steps:")
bfs_steps = water_jug_bfs(capacity1, capacity2, target)
print(bfs_steps if bfs_steps else "No solution found")
