import tkinter as tk
from tkinter import ttk
import sudoku

#  The first window that pops-up, lets you choose the difficulty with buttons/clicks
def start_game():
    window = tk.Tk()
    window.title("Sudoku Puzzle")
    window.geometry("300x200")
    window.minsize(width=300, height=200)

    label = tk.Label(window, text="Select Difficulty", font=("Arial", 14))
    label.pack(pady=15)

    button_easy = tk.Button(window, text="Easy", font=("Ariel", 10), width=15, command=lambda: load_sudoku("Easy", window))
    button_easy.pack(pady=(10,0))
    button_medium = tk.Button(window, text="Medium", font=("Ariel", 10), width=15, command=lambda: load_sudoku("Medium", window))
    button_medium.pack()
    button_hard = tk.Button(window, text="Hard", font=("Ariel", 10), width=15, command=lambda: load_sudoku("Hard", window))
    button_hard.pack()

    window.mainloop()

#  Make, fill and trim the board and then load the game logic/sudoku after choosing difficulty
def load_sudoku(difficulty, window):
    window.destroy()

    board = [[0 for _ in range(9)] for _ in range(9)]
    sudoku.fill_board(board)
    solution = [row[:] for row in board]

    if difficulty == "Easy":
        sudoku.trim_board_easy(board)
    elif difficulty == "Medium":
        sudoku.trim_board_medium(board)
    elif difficulty == "Hard":
        sudoku.trim_board_hard(board)

    open_game_window(board, solution)



#  Loads the window with the Sudoku puzzle so we can play
def open_game_window(board, solution):
    window = tk.Tk()
    window.title("Sudoku Puzzle")
    window.geometry("500x600")
    window.minsize(width=500, height=600)
    window.config(background="darkgrey", pady=5, padx=5)

    status_label = tk.Label(window, text="", font=("Arial", 14), highlightbackground="lightgrey", highlightthickness=2)
    status_label.grid(row=9, column=0, columnspan=9, pady=10, sticky="nsew")

    def validate_input(new_value):
        if new_value == "":
            return True
        if new_value.isdigit():
            number = int(new_value)
            if number >= 1 and number <= 9:
                return True
        return False

    vcmd = (window.register(validate_input), "%P")
    entries = [[None for _ in range(9)] for _ in range(9)]

    def check_entry(event, row, col):
        entry = entries[row][col]
        value = entry.get()

        number = int(value)
        if number == solution[row][col]:
            board[row][col] = number
            entry.config(bg="lightgreen", state="disabled")
            status_label.config(text="✅ Correct!", fg="green")
            
            if sudoku.board_is_full(board):
                status_label.config(text="🎉 Well done! 🎉", fg="blue")

        else:
            entry.delete(0, tk.END)
            entry.config(bg="red")
            status_label.config(text="❌ Nope! Try again.", fg="red")
            window.after(500, lambda: entry.config(bg="white"))

    def make_handler(r, c):
        return lambda e: check_entry(e, r, c)

    # Configure grid layout weights
    for i in range(9):
        window.columnconfigure(i, weight=1)
        window.rowconfigure(i, weight=1)

    # Add Sudoku cells
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                widget = tk.Entry(
                    window,
                    justify="center",
                    font=("Arial", 18),
                    width=2,
                    highlightthickness=2,
                    highlightbackground="lightgrey",
                    fg="black",
                    bg="lightgrey",
                )
                widget.insert(0, str(board[i][j]))
                widget.config(state="disabled")
            else:
                widget = tk.Entry(
                    window,
                    justify="center",
                    font=("Arial", 18),
                    width=2,
                    validate="key",
                    validatecommand=vcmd,
                    highlightthickness=2,
                    highlightbackground="lightgrey",
                    bg="white"
                )
                widget.bind("<Return>", make_handler(i, j))

            entries[i][j] = widget

            # Add borders for 3x3 grid separation
            top = 1
            left = 1
            right = 1
            bottom = 1

            if (i + 1) % 3 == 0 and i != 8:
                bottom = 5

            if (j + 1) % 3 == 0 and j != 8:
                right = 5

            widget.grid(row=i, column=j, padx=(left, right), pady=(top, bottom), sticky="nsew")

    window.mainloop()



start_game()


