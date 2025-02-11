# import tkinter as tk
# from tkinter import messagebox, simpledialog

# # Class to create the Tic Tac Toe game
# class TicTacToe:
#     def __init__(self, player_x="Player X", player_o="Player O"):
#         self.window = tk.Tk()
#         self.window.title("Tic Tac Toe")
#         self.window.config(bg="#f0f8ff")  # background color
#         self.window.geometry("700x400")  # window size (larger to fit the instructions)
#         self.player_x = player_x
#         self.player_o = player_o
#         self.current_player = self.player_x
#         self.current_symbol = "X"
#         self.board = [[" " for _ in range(3)] for _ in range(3)]
#         self.buttons = [[None for _ in range(3)] for _ in range(3)]
#         self.create_ui()

#     # Function to create the 3x3 grid of buttons
#     def create_ui(self):
#         # Create a frame for the game grid
#         game_frame = tk.Frame(self.window, bg="#f0f8ff")
#         game_frame.grid(row=0, column=0, padx=10, pady=10)

#         # Display current player's turn at the top
#         self.turn_label = tk.Label(game_frame, text=f"{self.current_player}'s turn for {self.current_symbol}", font=("Arial", 16), fg="blue", bg="#f0f8ff")
#         self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)

#         # Create the Tic Tac Toe grid (3x3)
#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col] = tk.Button(
#                     game_frame,
#                     text=" ",
#                     font=("Arial", 36),  # Increase font size for better visibility
#                     height=3,
#                     width=6,
#                     bg="#ffffff",  # White background for buttons
#                     activebackground="#ffcc00",  # Highlight color when clicked
#                     command=lambda r=row, c=col: self.on_click(r, c)
#                 )
#                 self.buttons[row][col].grid(row=row+1, column=col, padx=5, pady=5)  # Add padding for spacing

#         # Restart button
#         self.restart_button = tk.Button(game_frame, text="Restart Game", font=("Arial", 16), command=self.restart_game, bg="#4CAF50", fg="white")
#         self.restart_button.grid(row=4, column=0, columnspan=3, pady=20)

#         # Create a frame for the "How to play" section
#         instructions_frame = tk.Frame(self.window, bg="#f0f8ff")
#         instructions_frame.grid(row=0, column=1, padx=40, pady=50)

#         # Label to show instructions on how to play
#         self.instructions_label = tk.Label(
#             instructions_frame, 
#             text="How to Play:\n\n1. Players take turns.\n2. Click on an empty cell to place your mark.\n3. X starts first.\n4. The first to align 3 marks horizontally, vertically, or diagonally wins.\n5. If all cells are filled and no one wins, the game is a draw.", 
#             font=("Arial", 14), 
#             fg="white",  # White text color
#             bg="#6fa3ef",  # Light blue background (instruction panel)
#             justify="left",  # Left justify the text for better alignment
#             padx=10,  # Add padding to the left and right for spacing
#             pady=10,  # Add padding to the top and bottom for spacing
#             anchor="w"  # Align text to the left within the label
#         )
#         self.instructions_label.grid(row=0, column=0, sticky="w")

#     # Function to handle button clicks and set colors for X and O
#     def on_click(self, row, col):
#         if self.board[row][col] == " ":
#             self.board[row][col] = self.current_symbol
#             self.buttons[row][col].config(text=self.current_symbol)

#             # Set color for X and O
#             if self.current_symbol == "X":
#                 self.buttons[row][col].config(bg="lightblue")  # Color for X
#             else:
#                 self.buttons[row][col].config(bg="lightcoral")  # Color for O

#             if self.check_winner(row, col):
#                 winner = self.player_x if self.current_symbol == "X" else self.player_o
#                 messagebox.showinfo("Game Over", f"{winner} wins the game!")
#                 self.disable_buttons()
#             elif self.check_draw():
#                 messagebox.showinfo("Game Over", "It's a draw!")
#                 self.disable_buttons()
#             else:
#                 # Switch player
#                 self.switch_player()

#     # Function to switch the current player and update the label
#     def switch_player(self):
#         if self.current_symbol == "X":
#             self.current_symbol = "O"
#             self.current_player = self.player_o
#         else:
#             self.current_symbol = "X"
#             self.current_player = self.player_x
#         # Update the turn label
#         self.turn_label.config(text=f"{self.current_player}'s turn for {self.current_symbol}")

#     # Function to check for a winner
#     def check_winner(self, row, col):
#         # row
#         if all(self.board[row][i] == self.current_symbol for i in range(3)):
#             return True
#         # column
#         if all(self.board[i][col] == self.current_symbol for i in range(3)):
#             return True
#         # main diagonal
#         if row == col and all(self.board[i][i] == self.current_symbol for i in range(3)):
#             return True
#         # Check anti-diagonal
#         if row + col == 2 and all(self.board[i][2-i] == self.current_symbol for i in range(3)):
#             return True
#         return False

#     # Function to check for a draw
#     def check_draw(self):
#         return all(self.board[row][col] != " " for row in range(3) for col in range(3))

#     # Function to disable all buttons after game over
#     def disable_buttons(self):
#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col].config(state="disabled")

#     # Function to restart the game
#     def restart_game(self):
#         self.current_player = self.player_x
#         self.current_symbol = "X"
#         self.board = [[" " for _ in range(3)] for _ in range(3)]
#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col].config(text=" ", state="normal", bg="#ffffff")  # Reset color to white
#         self.turn_label.config(text=f"{self.current_player}'s turn for {self.current_symbol}")

#     # Function to run the game
#     def run(self):
#         self.window.mainloop()

# # Start the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Hide the initial window
#     player_x_name = simpledialog.askstring("Player X", "Enter Player X's name:") or "Player X"
#     player_o_name = simpledialog.askstring("Player O", "Enter Player O's name:") or "Player O"
#     game = TicTacToe(player_x=player_x_name, player_o=player_o_name)
#     game.run()




import tkinter as tk
from tkinter import messagebox, simpledialog

# Class to create the Tic Tac Toe game
class TicTacToe:
    def __init__(self, player_x="Player X", player_o="Player O"):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe (6x6)")
        self.window.config(bg="#f0f8ff")  # background color
        self.window.geometry("900x700")  # Larger window size for 6x6 grid
        self.player_x = player_x
        self.player_o = player_o
        self.current_player = self.player_x
        self.current_symbol = "X"
        self.board = [[" " for _ in range(6)] for _ in range(6)]  # 6x6 board
        self.buttons = [[None for _ in range(6)] for _ in range(6)]
        self.create_ui()

    # Function to create the 6x6 grid of buttons
    def create_ui(self):
        # Create a frame for the game grid
        game_frame = tk.Frame(self.window, bg="#f0f8ff")
        game_frame.grid(row=0, column=0, padx=10, pady=10)

        # Display current player's turn at the top
        self.turn_label = tk.Label(game_frame, text=f"{self.current_player}'s turn for {self.current_symbol}", font=("Arial", 16), fg="blue", bg="#f0f8ff")
        self.turn_label.grid(row=0, column=0, columnspan=6, pady=10)

        # Create the Tic Tac Toe grid (6x6)
        for row in range(6):
            for col in range(6):
                self.buttons[row][col] = tk.Button(
                    game_frame,
                    text=" ",
                    font=("Arial", 18),  # Font size adjusted for 6x6 grid
                    height=2,
                    width=5,
                    bg="#ffffff",
                    activebackground="#ffcc00",
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                self.buttons[row][col].grid(row=row+1, column=col, padx=3, pady=3)

        # Restart button
        self.restart_button = tk.Button(game_frame, text="Restart Game", font=("Arial", 16), command=self.restart_game, bg="#4CAF50", fg="white")
        self.restart_button.grid(row=7, column=0, columnspan=6, pady=20)

    # Function to handle button clicks
    def on_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_symbol
            self.buttons[row][col].config(text=self.current_symbol)

            # Set colors for X and O
            if self.current_symbol == "X":
                self.buttons[row][col].config(bg="lightblue")
            else:
                self.buttons[row][col].config(bg="lightcoral")

            if self.check_winner(row, col):
                winner = self.player_x if self.current_symbol == "X" else self.player_o
                messagebox.showinfo("Game Over", f"{winner} wins the game!")
                self.disable_buttons()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.disable_buttons()
            else:
                self.switch_player()

    # Function to switch players
    def switch_player(self):
        if self.current_symbol == "X":
            self.current_symbol = "O"
            self.current_player = self.player_o
        else:
            self.current_symbol = "X"
            self.current_player = self.player_x
        self.turn_label.config(text=f"{self.current_player}'s turn for {self.current_symbol}")

    # Function to check for a winner (4 in a row)
    def check_winner(self, row, col):
        directions = [
            (1, 0),  # vertical
            (0, 1),  # horizontal
            (1, 1),  # diagonal \
            (1, -1)  # diagonal /
        ]
        for dr, dc in directions:
            count = 1
            # Check forward
            r, c = row + dr, col + dc
            while 0 <= r < 6 and 0 <= c < 6 and self.board[r][c] == self.current_symbol:
                count += 1
                r += dr
                c += dc
            # Check backward
            r, c = row - dr, col - dc
            while 0 <= r < 6 and 0 <= c < 6 and self.board[r][c] == self.current_symbol:
                count += 1
                r -= dr
                c -= dc
            # Check if 4 in a row
            if count >= 4:
                return True
        return False

    # Function to check for a draw
    def check_draw(self):
        return all(self.board[row][col] != " " for row in range(6) for col in range(6))

    # Function to disable all buttons
    def disable_buttons(self):
        for row in range(6):
            for col in range(6):
                self.buttons[row][col].config(state="disabled")

    # Function to restart the game
    def restart_game(self):
        self.current_player = self.player_x
        self.current_symbol = "X"
        self.board = [[" " for _ in range(6)] for _ in range(6)]
        for row in range(6):
            for col in range(6):
                self.buttons[row][col].config(text=" ", state="normal", bg="#ffffff")
        self.turn_label.config(text=f"{self.current_player}'s turn for {self.current_symbol}")

    # Function to run the game
    def run(self):
        self.window.mainloop()

# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    player_x_name = simpledialog.askstring("Player X", "Enter Player X's name:") or "Player X"
    player_o_name = simpledialog.askstring("Player O", "Enter Player O's name:") or "Player O"
    game = TicTacToe(player_x=player_x_name, player_o=player_o_name)
    game.run()
