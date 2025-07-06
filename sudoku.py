#board = [[0 for i in range(9)] for j in range (9)]

board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 0, 0]
]

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
            if number==board[row][column]:
                return False
    return True

def insert_number(board, number, row, column):
    valid_row = number_is_valid_in_row(board=board, number=number, row=row)
    valid_column = number_is_valid_in_column(board=board, number=number, column=column)
    valid_box = number_is_valid_in_box(board=board, number=number, row=row, column=column)


    if valid_row and valid_column and valid_box:
        board[row][column] = number
        print("Success! Well done.")
    else:
        print("Invalid, please try again.")


print_board(board=board)
insert_number(board, 7, 8, 7)
print_board(board=board)
insert_number(board, 9, 8, 8)
print_board(board=board)