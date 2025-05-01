import numpy as np
class EightPuzzle:
    def __init__(self, initial_state):
        self.state = np.array(initial_state)
        self.goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Goal state

    def calculate_cost(self, state):
        """Calculate the Manhattan distance cost."""
        cost = 0
        for i in range(1, 9):  # Ignore 0 (blank space)
            x, y = np.where(state == i)
            gx, gy = np.where(self.goal == i)
            cost += abs(x[0] - gx[0]) + abs(y[0] - gy[0])
        return cost

    def get_neighbors(self, state):
        """Generate all possible moves."""
        neighbors = []
        x, y = np.where(state == 0)  # Locate the blank space
        x, y = x[0], y[0]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = state.copy()
                new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
                neighbors.append(new_state)
        return neighbors

    def hill_climbing(self):
        """Perform the Hill Climbing search."""
        current_state = self.state
        current_cost = self.calculate_cost(current_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            best_neighbor = None
            best_cost = current_cost

            for neighbor in neighbors:
                cost = self.calculate_cost(neighbor)
                if cost < best_cost:  # Lower cost is better
                    best_cost = cost
                    best_neighbor = neighbor

            if best_neighbor is None:  # No better state found
                return current_state, current_cost

            current_state = best_neighbor
            current_cost = best_cost
            print(f"Current Cost: {current_cost}\n{current_state}\n")

            if np.array_equal(current_state, self.goal):  # Goal reached
                return current_state, current_cost

# Example Usage
initial = [[1, 2, 3], 
           [0, 4, 6], 
           [7, 5, 8]]

puzzle = EightPuzzle(initial)
final_state, final_cost = puzzle.hill_climbing()

print("Final State:\n", final_state)
print("Final Cost:", final_cost)
