import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game state
current_player = "X"
board = [" " for _ in range(9)]

# Function to check if there's a winner
def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    return None

# Function to handle button clicks
def button_click(button, index):
    global current_player
    if board[index] == " " and check_winner() is None:
        board[index] = current_player
        button.config(text=current_player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        elif " " not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")

# Create the game board (3x3 grid of buttons)
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: button_click(buttons[i], i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create a reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 15), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Run the application
root.mainloop()