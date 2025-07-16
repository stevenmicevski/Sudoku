import tkinter as tk
import sudoku

board = [[0 for i in range(9)] for j in range (9)]
sudoku.fill_board(board)
sudoku.trim_board_easy(board)

window = tk.Tk()
window.title("Sudoku Puzzle")
window.geometry("600x600")

for i in range(9):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

    numbers = [[None for _ in range (9)] for _ in range (9)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            widget = tk.Entry(window, justify="center", font=("Arial", 18), width=2, highlightthickness=2, highlightbackground="black", background="lightgrey")
            widget.insert(0, str(board[i][j]))
            widget.config(state="disabled")
        else:
            widget = tk.Entry(window, justify="center", font=("Arial", 18), width=2, highlightthickness=2, highlightbackground="black", background="lightgrey")
            numbers[i][j] = widget

        top = 3 if i % 3 == 0 else 1
        left = 3 if j % 3 == 0 else 1
        right = 3 if j == 8 else 0
        bottom = 3 if i == 8 else 0

        widget.grid(row=i, column=j, sticky="nsew", padx=(left, right), pady=(top, bottom))


window.mainloop()