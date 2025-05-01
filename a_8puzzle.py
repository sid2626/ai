import heapq

goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    i, j = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == 0][0]
    
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

def best_first_search_8_puzzle(start_state):
    visited = set()
    heap = []
    heapq.heappush(heap, (manhattan_distance(start_state), start_state, []))

    while heap:
        cost, state, path = heapq.heappop(heap)
        state_t = tuple(tuple(row) for row in state)
        if state == goal_state:
            return path + [state]

        if state_t in visited:
            continue
        visited.add(state_t)

        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (manhattan_distance(neighbor), neighbor, path + [state]))
    return None

# Example usage
start = [[1,2,3],[4,0,6],[7,5,8]]
solution = best_first_search_8_puzzle(start)
for step in solution:
    for row in step:
        print(row)
    print("---")
