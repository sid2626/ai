def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def get_player_move(board):
    """Gets the player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")


def get_computer_move(board):
    """Computes the computer's move using simple logic."""
    # Try to win or block the opponent
    for player in ["O", "X"]:  # First check for winning moves, then for blocking moves
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board, player):
                        board[row][col] = " "  # Undo move
                        return row, col
                    board[row][col] = " "  # Undo move

    # Take center if available
    if board[1][1] == " ":
        return 1, 1

    # Take any corner
    for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[row][col] == " ":
            return row, col

    # Take any remaining space
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return row, col


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    is_player_turn = True

    while True:
        if is_player_turn:
            print("Your turn!")
            row, col = get_player_move(board)
            board[row][col] = "X"
        else:
            print("Computer's turn!")
            row, col = get_computer_move(board)
            board[row][col] = "O"

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        elif check_winner(board, "O"):
            print("Computer wins. Better luck next time!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        is_player_turn = not is_player_turn


if __name__ == "__main__":
    main()
