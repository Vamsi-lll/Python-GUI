# Import the libraries we need
import customtkinter as ctk  # This makes our window look modern
import tkinter.messagebox as msg  # This shows popup messages
import random  # This helps computer make random moves

# Set up how our window looks
ctk.set_appearance_mode("light")  # Makes the window bright/light colored
ctk.set_default_color_theme("blue")  # Makes buttons and highlights blue

# Create the main window for our game
app = ctk.CTk()
app.title("Tic Tac Toe vs Computer")  # Set the title at the top of window

# Create variables to store game information
player = "X"  # Keep track of whose turn it is (X = human, O = computer)
board = [["" for _ in range(3)] for _ in range(3)]  # Create empty 3x3 grid to store moves

# This function runs when a human player clicks on a button
def on_click(r, c):
    global player  # We need to change the player variable
    
    # Check if the clicked square is empty (no X or O in it)
    if board[r][c] == "":
        board[r][c] = player  # Put the current player's symbol in that square
        buttons[r][c].configure(text=player)  # Show X or O on the button
        
        # Check if this move wins the game
        if check_winner(player):
            msg.showinfo("Game Over", f"Player {player} wins!")  # Show winning message
            reset_board()  # Start a new game
        # Check if all squares are filled (it's a draw)
        elif all(all(cell != "" for cell in row) for row in board):
            msg.showinfo("Game Over", "It's a draw!")  # Show draw message
            reset_board()  # Start a new game
        else:
            # Game continues, switch to computer's turn
            player = "O"
            app.after(500, computer_move)  # Wait half second, then computer moves

# This function makes the computer play its turn
def computer_move():
    global player  # We need to change the player variable

    # STEP 1: Try to win the game
    # Computer checks every empty square to see if it can win
    for r in range(3):  # Check each row (0, 1, 2)
        for c in range(3):  # Check each column (0, 1, 2)
            if board[r][c] == "":  # If this square is empty
                board[r][c] = player  # Pretend to put O there
                if check_winner(player):  # Would this win the game?
                    buttons[r][c].configure(text=player)  # Actually put O there
                    msg.showinfo("Game Over", "Computer wins!")  # Show winning message
                    reset_board()  # Start new game
                    return  # Stop here, computer won
                board[r][c] = ""  # Remove the pretend move, keep looking

    # STEP 2: Try to block the human player from winning
    # Computer checks if human can win on next move and blocks it
    for r in range(3):  # Check each row
        for c in range(3):  # Check each column
            if board[r][c] == "":  # If this square is empty
                board[r][c] = "X"  # Pretend human puts X there
                if check_winner("X"):  # Would human win?
                    board[r][c] = player  # Put O there to block human
                    buttons[r][c].configure(text=player)  # Show O on button
                    player = "X"  # Switch back to human's turn
                    return  # Stop here, successfully blocked human
                board[r][c] = ""  # Remove pretend move, keep checking

    # STEP 3: If can't win or block, just pick any empty square randomly
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]  # Find all empty squares
    if empty_cells:  # If there are empty squares available
        r, c = random.choice(empty_cells)  # Pick one randomly
        board[r][c] = player  # Put O in that square
        buttons[r][c].configure(text=player)  # Show O on the button

    # After computer's move, check if game is over
    if check_winner(player):  # Did computer win?
        msg.showinfo("Game Over", "Computer wins!")  # Show winning message
        reset_board()  # Start new game
    elif all(all(cell != "" for cell in row) for row in board):  # Are all squares filled?
        msg.showinfo("Game Over", "It's a draw!")  # Show draw message
        reset_board()  # Start new game
    else:
        player = "X"  # Switch back to human player's turn

# This function checks if someone has won the game
def check_winner(p):  # p is the player we're checking (X or O)
    return any(
        # Check if any row has 3 in a row (horizontal win)
        all(board[i][j] == p for j in range(3)) or
        # Check if any column has 3 in a row (vertical win)
        all(board[j][i] == p for j in range(3))
        for i in range(3)  # Do this check for all 3 rows and columns
    # Check diagonal from top-left to bottom-right
    ) or all(board[i][i] == p for i in range(3)) or all(board[i][2 - i] == p for i in range(3))
    # Check diagonal from top-right to bottom-left

# This function starts a new game by clearing everything
def reset_board():
    global board, player  # We need to change these variables
    player = "X"  # Human always goes first
    board = [["" for _ in range(3)] for _ in range(3)]  # Make all squares empty again
    # Clear all the buttons so they show nothing
    for r in range(3):  # Go through each row
        for c in range(3):  # Go through each column
            buttons[r][c].configure(text="")  # Make button show nothing

# Create the visual part of the game (the buttons you click)
frame = ctk.CTkFrame(app)  # Create a container to hold all the buttons
frame.pack(padx=20, pady=20)  # Put some space around the container

# Create a 3x3 grid of buttons (9 buttons total)
# Each button represents one square on the tic-tac-toe board
buttons = [[ctk.CTkButton(frame, text="", width=100, height=100, font=('Helvetica', 24),
                          command=lambda r=r, c=c: on_click(r, c)) for c in range(3)] for r in range(3)]
# This creates: buttons[0][0], buttons[0][1], buttons[0][2] (top row)
#               buttons[1][0], buttons[1][1], buttons[1][2] (middle row)
#               buttons[2][0], buttons[2][1], buttons[2][2] (bottom row)

# Put each button in the right place on the screen
for r in range(3):  # For each row (0, 1, 2)
    for c in range(3):  # For each column (0, 1, 2)
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)  # Place button with some spacing

# Start the game! This makes the window appear and wait for clicks
app.mainloop()
