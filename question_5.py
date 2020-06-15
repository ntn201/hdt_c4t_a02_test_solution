def get_move(board,row,col):
    moves = []
    for i in [-1,1]:
            if 0 <= row+i < len(board):
                if board[row+i][col] != "*":
                    moves.append((row+i,col))
    for j in [-1,1]:
            if 0 <= col+j < len(board[0]):
                if board[row][col+j] != "*":
                    moves.append((row,col+j))
    return moves

def print_board(board):
    for row in board:
        print(row)
    print()

def go(board,i=0,j=0,string=""):
    if string == "Vinh":
        print_board(board)
    else:
        if string+board[i][j] == "Vinh":
            temp = board[i][j]
            board[i][j] = "*"
            print_board(board)
            board[i][j] = temp
        moves = get_move(board,i,j)
        for move in moves:
            temp = board[i][j]
            board[i][j] = "*"
            go(board,move[0],move[1],string+temp)
            board[i][j] = temp


board = [["V","i","n","h"],
         ["i","n","h"," "],
         ["n","h"," "," "],
         ["h"," "," "," "]]

go(board)