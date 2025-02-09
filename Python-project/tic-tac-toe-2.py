import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Class to create the Tic Tac Toe game (One Player vs. Computer)
class TicTacToe:
    def __init__(self, player_name="Player"):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - Player vs Computer")
        self.window.config(bg="#f0f8ff")  # Set background color
        self.window.geometry("600x700")  # Set window size
        self.player_name = player_name
        self.computer_name = "Computer"
        self.current_player = self.player_name
        self.current_symbol = "X"  # Player is X, Computer is O
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_ui()

    # Function to create the 3x3 grid of buttons
    def create_ui(self):
        # Display current player's turn at the top
        self.turn_label = tk.Label(self.window, text=f"{self.current_player}'s turn for {self.current_symbol}", font=("Arial", 16), fg="blue", bg="#f0f8ff")
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create the Tic Tac Toe grid (3x3)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window,
                    text=" ",
                    font=("Arial", 36),  # Increase font size for better visibility
                    height=3,
                    width=6,
                    bg="#ffffff",  # White background for buttons
                    activebackground="#ffcc00",  # Highlight color when clicked
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                self.buttons[row][col].grid(row=row+1, column=col, padx=10, pady=10)  # Add padding for spacing

        # Restart button
        self.restart_button = tk.Button(self.window, text="Restart Game", font=("Arial", 16), command=self.restart_game, bg="#4CAF50", fg="white")
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=20)

        # Create the instructions frame
        instructions_frame = tk.Frame(self.window, bg="#f0f8ff")
        instructions_frame.grid(row=0, column=0, columnspan=3, padx=40, pady=50)

        # Label to show instructions on how to play
        self.instructions_label = tk.Label(
            instructions_frame, 
            text="How to Play:\n\n1. Players take turns.\n2. Click on an empty cell to place your mark.\n3. X starts first.\n4. The first to align 3 marks horizontally, vertically, or diagonally wins.\n5. If all cells are filled and no one wins, the game is a draw.", 
            font=("Arial", 14), 
            fg="white",  # White text color for better contrast
            bg="#6fa3ef",  # Light blue background for the instruction panel
            justify="left",  # Left justify the text for better alignment
            padx=10,  # Add padding to the left and right for spacing
            pady=10,  # Add padding to the top and bottom for spacing
            anchor="w"  # Align text to the left within the label
        )
        self.instructions_label.grid(row=0, column=0, sticky="w")

    # Function to handle button clicks
    def on_click(self, row, col):
        if self.board[row][col] == " " and self.current_player == self.player_name:
            self.board[row][col] = self.current_symbol
            self.buttons[row][col].config(text=self.current_symbol)
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"{self.player_name} wins!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                # Switch to computer's turn
                self.switch_player()
                self.computer_move()

    # Function to switch the current player
    def switch_player(self):
        if self.current_symbol == "X":
            self.current_symbol = "O"
            self.current_player = self.computer_name
        else:
            self.current_symbol = "X"
            self.current_player = self.player_name
        # Update the turn label
        self.turn_label.config(text=f"{self.current_player}'s turn for {self.current_symbol}")

    # Function to make the computer's move
    def computer_move(self):
        # Randomly choose an empty spot for the computer to make a move
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
        if available_moves:
            move = random.choice(available_moves)
            row, col = move
            self.board[row][col] = self.current_symbol
            self.buttons[row][col].config(text=self.current_symbol)
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"{self.computer_name} wins!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                # Switch to player's turn
                self.switch_player()

    # Function to check for a winner
    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][i] == self.current_symbol for i in range(3)):
            return True
        # Check column
        if all(self.board[i][col] == self.current_symbol for i in range(3)):
            return True
        # Check main diagonal
        if row == col and all(self.board[i][i] == self.current_symbol for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.board[i][2-i] == self.current_symbol for i in range(3)):
            return True
        return False

    # Function to check for a draw
    def check_draw(self):
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))

    # Function to disable all buttons after game over
    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state="disabled")

    # Function to restart the game
    def restart_game(self):
        self.current_player = self.player_name
        self.current_symbol = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", state="normal", bg="#ffffff")  # Reset color to white
        self.turn_label.config(text=f"{self.current_player}'s turn for {self.current_symbol}")

    # Function to run the game
    def run(self):
        self.window.mainloop()

# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the initial window
    player_name = simpledialog.askstring("Player", "Enter your name:") or "Player"
    game = TicTacToe(player_name=player_name)
    game.run()
