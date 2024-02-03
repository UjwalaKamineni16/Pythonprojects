import random

# Define an empty board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Function to check if the board is filled
def is_board_filled():
    for row in board:
        for element in row:
            if element == '-':
                return False
    return True

# Function to check if a player has won
def is_winner(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

# Function to show the board
def show_board():
    for row in board:
        print(row)

# Function to start the game
def start_game():
    # Select first turn randomly
    current_player = random.choice(['X', 'O'])
    
    # Loop until game is over
    while True:
        # Show the board
        show_board()
        
        # Ask for player's input
        try:
            row = int(input(f"{current_player}'s turn. Enter row number (1-3): ")) - 1
            col = int(input(f"{current_player}'s turn. Enter column number (1-3): ")) - 1
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue
        
        # Check if the move is legal
        if board[row][col] != '-':
            print("Illegal move! Please select an empty spot.")
            continue
        
        # Update the board with player's move
        board[row][col] = current_player
        
        # Check if the current player has won
        if is_winner(current_player):
            show_board()
            print(f"{current_player} wins!")
            break
        
        # Check if the board is filled
        if is_board_filled():
            show_board()
            print("Draw!")
            break
        
        # Switch to the other player's turn
        current_player = 'X' if current_player == 'O' else 'O'
    
    # Show the final view of the board
    show_board()

# Start the game
start_game()
