board = [[0 for i in range(9)] for j in range (9)];

def print_board(board):
    for i in range(9):
        if i%3==0:
            print("+-------+-------+-------+");
        for j in range(9):
            if j%3==0:
                print("|", end=" ");
            print (board[i][j], end=" "); 
        print("|");
    print("+-------+-------+-------+");

print_board(board=board);