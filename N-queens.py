import tkinter as tk
from random import randint, shuffle

class NQueensHillClimbing:
    def __init__(self, N):
        self.N = N
        self.board = [0] * N
        self.hill_climbing()

    def hill_climbing(self):
        self.board = [randint(0, self.N - 1) for _ in range(self.N)]
        while True:
            current_heuristic = self.heuristic(self.board)
            if current_heuristic == 0:
                break
            best_heuristic = current_heuristic
            best_board = self.board[:]
            for col in range(self.N):
                for row in range(self.N):
                    if self.board[col] == row:
                        continue
                    new_board = self.board[:]
                    new_board[col] = row
                    new_heuristic = self.heuristic(new_board)
                    if new_heuristic < best_heuristic:
                        best_heuristic = new_heuristic
                        best_board = new_board
            if best_heuristic == current_heuristic:
                break
            self.board = best_board

    def heuristic(self, board):
        conflicts = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

class NQueensGUI:
    def __init__(self, master, size):
        self.master = master
        self.master.title("N-Queens Solver")
        self.size = size
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        self.solve_button.pack()
        self.board = None

    def solve(self):
        n_queens = NQueensHillClimbing(self.size)
        self.board = n_queens.board
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 400 // self.size
        for i in range(self.size):
            for j in range(self.size):
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color)
                if self.board[i] == j:
                    self.canvas.create_oval(j * cell_size + 5, i * cell_size + 5, (j + 1) * cell_size - 5, (i + 1) * cell_size - 5, fill="red")

def main():
    root = tk.Tk()
    size = 4  # You can change the board size here
    gui = NQueensGUI(root, size)
    root.mainloop()

if __name__ == "__main__":
    main()
