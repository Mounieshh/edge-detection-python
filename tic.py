from collections import deque

# The game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if a player has won
def has_won(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the game is a draw
def is_draw(board):
    return all(cell == ' ' for row in board for cell in row)

# Function to perform BFS
def bfs(board, player):
    queue = deque([(board, player)])
    while queue:
        board, player = queue.popleft()
        if has_won(board, player):
            return board
        if is_draw(board):
            return board
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    new_board = [row[:] for row in board]
                    new_board[i][j] = player
                    queue.append((new_board, 'O' if player == 'X' else 'X'))
    return None

# Initialize the game board
print_board(board)

# Perform BFS
result = bfs(board, 'X')

# Print the result
if result:
    print_board(result)
    if has_won(result, 'X'):
        print("X wins!")
    elif has_won(result, 'O'):
        print("O wins!")
    else:
        print("It's a draw!")
else:
    print("No solution found!")