import tkinter as tk
from tkinter import messagebox

# Define the game board
board = [[' ' for _ in range(10)] for _ in range(10)]

# Define Board & Players
players = ['red', 'yellow']
current_player = players[0]
board_size = 10

# Define the number of rows & columns in the board
num_rows = num_cols = 10 

# Define the Winning Sequence and Empty Cell Length
win_seq_len = 4
empty_cell = ' '

# function to check if a player has won
def check_win(player, board):
    for i in range(num_rows):
        for j in range(num_cols - win_seq_len + 1):
            if all([board[i][j + k] == player for k in range(win_seq_len)]):
                return True
    for i in range(num_rows - win_seq_len + 1):
        for j in range(num_cols):
            if all([board[i + k][j] == player for k in range(win_seq_len)]):
                return True
    for i in range(num_rows - win_seq_len + 1):
        for j in range(num_cols - win_seq_len + 1):
            if all([board[i + k][j + k] == player for k in range(win_seq_len)]):
                return True
    for i in range(num_rows - win_seq_len + 1):
        for j in range(num_cols - win_seq_len + 1):
            if all([board[i + k][j + (win_seq_len - 1) - k] == player for k in range(win_seq_len)]):
                return True
    return False

# Switching to Next Player...
def get_next_player(player):
    return players[(players.index(player) + 1) % 2]

def num_empty_cells(row):
    return row.count(empty_cell)

# function to check if the board is full
def is_full(board):
    for row in board:
        if empty_cell in row:
            return False
    return True

# function to add a token to the board
def add_token(player, col, board):
    for i in range(num_rows - 1, -1, -1):
        if board[i][col] == empty_cell:
            board[i][col] = player
            break

# function to handle button click
def button_click(col):
    global current_player
    if num_empty_cells(board[0]) > 0:
        add_token(current_player, col, board)
        update_board()
        if check_win(current_player, board):
            messagebox.showinfo("Game Over", f"{current_player} wins!")
            reset_board()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = get_next_player(current_player)

# function to update the GUI board
def update_board():
    for i in range(num_rows):
        for j in range(num_cols):
            buttons[i][j].config(text=board[i][j])

# function to reset the board
def reset_board():
    global board
    board = [[' ' for _ in range(10)] for _ in range(10)]
    update_board()

# create the main window
root = tk.Tk()
root.title("Connect Four")

# create the buttons for the board
buttons = [[None for _ in range(num_cols)] for _ in range(num_rows)]
for i in range(num_rows):
    for j in range(num_cols):
        button = tk.Button(root, text=' ', width=5, height=2, command=lambda j=j: button_click(j))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# start the main event loop
root.mainloop()
