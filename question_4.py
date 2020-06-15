def print_board(board):
    for i in range(len(board)): 
        for j in range(len(board)): 
            print(board[i][j],end =' ') 
        print() 
    print()

def get_moves(board,row,col):
    moves = []
    for i in [-1,1]:
        for j in [-2,2]:
            if 0 <= row+i < len(board) and 0 <= col+j < len(board):
                if board[row+i][col+j] == -1:
                    moves.append((row+i,col+j))
    for i in [-2,2]:
        for j in [-1,1]:
            if 0 <= row+i < len(board) and 0 <= col+j < len(board):
                if board[row+i][col+j] == -1:
                    moves.append((row+i,col+j)) 
    return moves

def go(board,row=0,col=0,pos=1):
    if pos == len(board)**2:
        board[row][col] = pos
        print_board(board)
        print()
        board[row][col] = -1
    else:
        moves = get_moves(board,row,col)
        for move in moves:
            board[row][col] = pos
            go(board,move[0],move[1],pos+1)
            board[row][col] = -1

n = int(input("Nhap vao so N: "))
board = [[-1 for i in range(n)] for j in range(n)]
go(board,2,2)