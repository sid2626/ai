import math

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board with labels
def print_board(board):
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  ---+---+---")
    print()

# Function to check for a winner or draw
def check_winner(board):
    # Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check for draw
    for row in board:
        if ' ' in row:
            return None
    return 'Draw'

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == 'O':
        return 1
    elif result == 'X':
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Get the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function to play the game
def play_game():
    print("\n🎮 Welcome to Tic Tac Toe (You = X | AI = O)")
    print_board(board)

    while True:
        # User Move
        while True:
            try:
                row = int(input("👉 Enter your move (row 0-2): "))
                col = int(input("👉 Enter your move (col 0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("❌ Invalid move! Cell already taken or out of bounds. Try again.")
            except ValueError:
                print("❌ Invalid input! Please enter numbers only (0 to 2).")

        print("\n🧑 Your move:")
        print_board(board)

        result = check_winner(board)
        if result:
            if result == 'Draw':
                print("🤝 It's a Draw!")
            elif result == 'X':
                print("🏆 You Win! 🎉")
            else:
                print("🤖 AI Wins! 💻")
            break

        # AI Move
        print("🤖 AI is thinking...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'O'

        print("\n🤖 AI played:")
        print_board(board)

        result = check_winner(board)
        if result:
            if result == 'Draw':
                print("🤝 It's a Draw!")
            elif result == 'X':
                print("🏆 You Win! ")
            else:
                print("🤖 AI Wins! ")
            break


# Start the game
if __name__ == "__main__":
    play_game()
