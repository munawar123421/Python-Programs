import tkinter as tk from tkinter import messagebox

class TicTacToe: def init(self, root): self.root = root self.root.title("Tic Tac Toe") self.current_player = "X" self.board = [[" " for _ in range(3)] for _ in range(3)] self.buttons = [[None for _ in range(3)] for _ in range(3)] self.create_widgets()

def create_widgets(self):
    for row in range(3):
        for col in range(3):
            button = tk.Button(self.root, text=" ", font='Helvetica 20', height=2, width=5,
                               command=lambda row=row, col=col: self.on_click(row, col))
            button.grid(row=row, column=col)
            self.buttons[row][col] = button

def on_click(self, row, col):
    if self.board[row][col] == " ":
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        if self.check_win(self.current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.reset_board()
        elif self.check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.reset_board()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

def check_win(self, player):
    for row in self.board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([self.board[row][col] == player for row in range(3)]):
            return True

    if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def check_draw(self):
    for row in self.board:
        if " " in row:
            return False
    return True

def reset_board(self):
    self.board = [[" " for _ in range(3)] for _ in range(3)]
    self.current_player = "X"
    for row in range(3):
        for col in range(3):
            self.buttons[row][col].config(text=" ")
if name == "main": root = tk.Tk() game = TicTacToe(root) root.mainloop()
