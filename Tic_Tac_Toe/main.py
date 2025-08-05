import customtkinter as ctk
import tkinter.messagebox as msg
import random

# GUI Settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Tic Tac Toe vs Computer")

# Game variables
player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

def on_click(r, c):
    global player
    if board[r][c] == "":
        board[r][c] = player
        buttons[r][c].configure(text=player)
        if check_winner(player):
            msg.showinfo("Game Over", f"Player {player} wins!")
            reset_board()
        elif all(all(cell != "" for cell in row) for row in board):
            msg.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            player = "O"
            app.after(500, computer_move)

def computer_move():
    global player

    # Try to win
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = player
                if check_winner(player):
                    buttons[r][c].configure(text=player)
                    msg.showinfo("Game Over", "Computer wins!")
                    reset_board()
                    return
                board[r][c] = ""

    # Try to block player X
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "X"
                if check_winner("X"):
                    board[r][c] = player
                    buttons[r][c].configure(text=player)
                    player = "X"
                    return
                board[r][c] = ""

    # Otherwise, pick a random move
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = player
        buttons[r][c].configure(text=player)

    if check_winner(player):
        msg.showinfo("Game Over", "Computer wins!")
        reset_board()
    elif all(all(cell != "" for cell in row) for row in board):
        msg.showinfo("Game Over", "It's a draw!")
        reset_board()
    else:
        player = "X"

def check_winner(p):
    return any(
        all(board[i][j] == p for j in range(3)) or
        all(board[j][i] == p for j in range(3))
        for i in range(3)
    ) or all(board[i][i] == p for i in range(3)) or all(board[i][2 - i] == p for i in range(3))

def reset_board():
    global board, player
    player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            buttons[r][c].configure(text="")

# Create grid of buttons
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20)

buttons = [[ctk.CTkButton(frame, text="", width=100, height=100, font=('Helvetica', 24),
                          command=lambda r=r, c=c: on_click(r, c)) for c in range(3)] for r in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

app.mainloop()
