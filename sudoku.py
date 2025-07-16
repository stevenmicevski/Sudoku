import random
import copy

#  Prints the board
def print_board(board):
    for i in range(9):
        if i%3==0:
            print("+-------+-------+-------+")
        for j in range(9):
            if j%3==0:
                print("|", end=" ")
            print (board[i][j], end=" "); 
        print("|");
    print("+-------+-------+-------+")

#  Checks if the number we want to insert is valid in the row.
def number_is_valid_in_row(board, number, row):
    for i in board[row]:
        if number==i:
            return False
    return True

#  Checks if the number we want to insert is valid in the column.
def number_is_valid_in_column(board, number, column):
    for i in board:
        if number==i[column]:
            return False
    return True

#  Checks if the number we want to insert is valid in the box.
def number_is_valid_in_box(board, number, row, column):
    start_row = (row//3) * 3
    start_column = (column//3) * 3
    for i in range(start_row, start_row+3):
        for j in range(start_column, start_column+3):
            if number==board[i][j]:
                return False
    return True

#  Inserts a number in the board, first checks if the inserion is valid in every row/column/box.
def insert_number(board, number, row, column):
    valid_row = number_is_valid_in_row(board, number, row)
    valid_column = number_is_valid_in_column(board, number, column)
    valid_box = number_is_valid_in_box(board, number, row, column)

    if valid_row and valid_column and valid_box:
        board[row][column] = number
        print("Success!")
    else:
        print("Invalid, please try again.")

#  Automatically solves/fills the board recursively, first it makes a list with shuffled numbers 1 through 9, picks a number and checks if the insertion is valid, if it is, it places the number, then recursively tries to fill the rest of the board, if it succeeds it returns True, if not, it resets the placed number to 0,  and tries again with another number, if every number fails, it returns False and the previous number gets reset to 0, and tries again with another number, etc.
def fill_board(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] != 0:
                    continue
            numbers = [i for i in range(1,10)]
            random.shuffle(numbers)
            for i in numbers:
                if number_is_valid_in_row(board, i, row) and number_is_valid_in_column(board, i, column) and number_is_valid_in_box(board, i, row, column):
                    board[row][column] = i
                    if fill_board(board):
                        return True
                    else:
                        board[row][column] = 0
            return False
    return True

#  Counts the number of solutions recursively, checks if the board hase only 1 unique solution.
def count_solutions(board):
    if board_is_full:
        return 1
    
    solutions = 0
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                for i in range(1,10):
                    if number_is_valid_in_row(board, i, row) and number_is_valid_in_column(board, i, column) and number_is_valid_in_box(board, i, row, column):
                        board[row][column] = i
                        solutions = solutions + count_solutions(board)
                        board[row][column] = 0
                        if solutions > 1:
                            return solutions
                return solutions
    return solutions

#  Trims the automatically filled board to Easy difficulty so it's playable, but before triming each number it checks if the board still has only 1 solution.
def trim_board_easy(board):
    i = 0
    while i < 31:
        cell = random.randint(0, 80)
        row = cell // 9
        column = cell % 9
        if board[row][column] != 0:
            tmpboard = copy.deepcopy(board)
            tmpboard[row][column] = 0
            if count_solutions(tmpboard) == 1:
                board[row][column] = 0
                i = i + 1

#  Trims the automatically filled board to Medium difficulty so it's playable, but before triming each number it checks if the board still has only 1 solution.
def trim_board_medium(board):
    i = 0
    while i < 38:
        cell = random.randint(0, 80)
        row = cell // 9
        column = cell % 9
        if board[row][column] != 0:
            tmpboard = copy.deepcopy(board)
            tmpboard[row][column] = 0
            if count_solutions(tmpboard) == 1:
                board[row][column] = 0
                i = i + 1

#  Trims the automatically filled board to Hard difficulty so it's playable, but before triming each number it checks if the board still has only 1 solution.
def trim_board_hard(board):
    i = 0
    while i < 46:
        cell = random.randint(0, 80)
        row = cell // 9
        column = cell % 9
        if board[row][column] != 0:
            tmpboard = copy.deepcopy(board)
            tmpboard[row][column] = 0
            if count_solutions(tmpboard) == 1:
                board[row][column] = 0
                i = i + 1

#  Checks if the board is full
def board_is_full(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return False
    return True

#  Lets the player to choose a diffiulty
def select_difficulty(board):
    difficulty = input("Choose difficulty (Easy, Medium, Hard): ")
    difficulty = difficulty.capitalize()
    while difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard":
        difficulty = input("Invalid selection, please try again: ")
        difficulty = difficulty.capitalize()
    if difficulty == "Easy":
        trim_board_easy(board)
    elif difficulty == "Medium":
        trim_board_medium(board)
    elif difficulty == "Hard":
        trim_board_hard(board)

#  Generates a board and Starts a Sudoku game
def start_game():
    board = [[0 for i in range(9)] for j in range (9)]
    fill_board(board)
    select_difficulty(board)
    print("Game started!")
    print_board(board)
    while board_is_full(board) != True:
        print("Insert a number: ")
        number = input("number: ")
        row = input("row: ")
        column = input ("column: ")
        insert_number(board, int(number), int(row)-1, int(column)-1)
        print_board(board)
    print("WELL DONE!")
    print_board(board)
