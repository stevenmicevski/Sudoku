import random

board = [[0 for i in range(9)] for j in range (9)]

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


def number_is_valid_in_row(board, number, row):
    for i in board[row]:
        if number==i:
            return False
    return True


def number_is_valid_in_column(board, number, column):
    for i in board:
        if number==i[column]:
            return False
    return True


def number_is_valid_in_box(board, number, row, column):
    start_row = (row//3) * 3
    start_column = (column//3) * 3
    for i in range(start_row, start_row+3):
        for j in range(start_column, start_column+3):
            if number==board[i][j]:
                return False
    return True


def insert_number(board, number, row, column):
    valid_row = number_is_valid_in_row(board, number, row)
    valid_column = number_is_valid_in_column(board, number, column)
    valid_box = number_is_valid_in_box(board, number, row, column)

    if valid_row and valid_column and valid_box:
        board[row][column] = number
        print("Success! Well done.")
    else:
        print("Invalid, please try again.")


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

#def trim_board(board):


fill_board(board)
print_board(board)

difficulty = input("Choose difficulty (Easy, Medium, Hard): ")
while difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard":
        difficulty = input("Invalid selection, please try again: ")
print(difficulty)