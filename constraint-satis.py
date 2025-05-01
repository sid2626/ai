from itertools import permutations
import matplotlib.pyplot as plt
import networkx as nx

# a. CRYPTARITHMETIC
def cryptarithmetic():
    print("\n--- Cryptarithmetic Problem ---")
    print("Format: WORD1 + WORD2 = RESULT")
    eq = input("Enter equation: ").replace(" ", "")
    if '+' not in eq or '=' not in eq:
        print("Invalid format!")
        return

    word1, rest = eq.split('+')
    word2, result = rest.split('=')
    unique_chars = set(word1 + word2 + result)
    if len(unique_chars) > 10:
        print("Too many unique letters (max 10).")
        return

    letters = ''.join(unique_chars)
    for p in permutations(range(10), len(letters)):
        table = dict(zip(letters, p))
        if table[word1[0]] == 0 or table[word2[0]] == 0 or table[result[0]] == 0:
            continue
        num1 = int(''.join(str(table[c]) for c in word1))
        num2 = int(''.join(str(table[c]) for c in word2))
        res = int(''.join(str(table[c]) for c in result))
        if num1 + num2 == res:
            print(f"\nSolution:")
            print(f"{word1}: {num1}")
            print(f"{word2}: {num2}")
            print(f"{result}: {res}")
            return
    print("No solution found.")

# b. CROSSWORD PUZZLE
def crossword_puzzle():
    print("\n--- Crossword Puzzle ---")
    size = int(input("Enter grid size (e.g., 3 for 3x3): "))
    words = input(f"Enter {size} words of length {size} (comma-separated): ").split(',')

    if any(len(w) != size for w in words):
        print("Each word must be same length as grid size.")
        return

    grid = [['_' for _ in range(size)] for _ in range(size)]

    def is_valid_horizontal(row, word):
        return all(grid[row][col] == '_' or grid[row][col] == word[col] for col in range(size))

    def is_valid_vertical(col, word):
        return all(grid[row][col] == '_' or grid[row][col] == word[row] for row in range(size))

    def place_horizontal(row, word):
        for col in range(size):
            grid[row][col] = word[col]

    def place_vertical(col, word):
        for row in range(size):
            grid[row][col] = word[row]

    def solve(idx):
        if idx == len(words):
            return True
        word = words[idx]
        for i in range(size):
            if is_valid_horizontal(i, word):
                old = grid[i][:]
                place_horizontal(i, word)
                if solve(idx + 1):
                    return True
                grid[i] = old[:]
            if is_valid_vertical(i, word):
                old = [grid[r][i] for r in range(size)]
                place_vertical(i, word)
                if solve(idx + 1):
                    return True
                for r in range(size):
                    grid[r][i] = old[r]
        return False

    if solve(0):
        print("\nFinal Grid:")
        for row in grid:
            print(' '.join(row))
    else:
        print("No solution found.")

# c. MAP COLORING PROBLEM 
def map_coloring():
    print("\n--- Map Coloring Problem ---")
    n = int(input("Enter number of regions: "))
    regions = []
    neighbors = {}

    for i in range(n):
        region = input(f"Enter name of region {i+1}: ")
        regions.append(region)
        neighbors[region] = []

    for region in regions:
        adj = input(f"Enter neighbors of {region} (comma-separated): ").split(',')
        neighbors[region] = [a.strip() for a in adj if a.strip() in regions and a.strip() != region]

    colors = input("Enter available colors (comma-separated): ").split(',')
    assignment = {}

    def is_valid(region, color):
        return all(assignment.get(nei) != color for nei in neighbors[region])

    def backtrack(index):
        if index == len(regions):
            return True
        region = regions[index]
        for color in colors:
            if is_valid(region, color):
                assignment[region] = color
                if backtrack(index + 1):
                    return True
                del assignment[region]
        return False

    if backtrack(0):
        print("\nRegion Colors:")
        for region in regions:
            print(f"{region}: {assignment[region]}")
    else:
        print("No solution found.")

# Menu
def main():
    while True:
        print("\n===== Constraint Satisfaction Problems =====")
        print("1. Cryptarithmetic")
        print("2. Crossword Puzzle")
        print("3. Map Coloring")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            cryptarithmetic()
        elif choice == '2':
            crossword_puzzle()
        elif choice == '3':
            map_coloring()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
