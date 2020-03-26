import sys

board_test = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

'''
The function returns an empty coordinates if it exists.
Argument:
    --board : Array(board of sudoku)
Return:
    --(i,j) : (int,int) coordinates empty.
'''
def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

'''
Function that checks whether the digit at a position is correct.
Arguments:
    --board : --Array() board of sudoku.
    --num : int() digit.
    --pos : coordinates. 
'''
def valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    squareX = pos[1]//3
    squareY = pos[0]//3
    for i in range(squareY*3, squareY*3+3):
        for j in range(squareX*3, squareX*3+3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

'''
The function prints the board.
Argument:
    -- board : --Array(board of sudoku).
Return:
    None.
'''
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

'''The function transforms a character string into an exploitable table for the solver.
Arguments :
    -boardMain : --str (board of sudoku in string).
Return:
    - : --Array (new board of sudoku).
'''
def substitution(boardMain):
    tmp= [[0] * 9]*9
    for i in range(9):
        for j in range(9):
            tmp[i][j] = int(boardMain[i*9+j])
    return tmp


def main(board):
    '''Main function.
    '''
    if (len(sys.argv) == 1 ):
        boardMain = str(input("Give your sudoku board :"))
        board = substitution(boardMain)
    elif (len(sys.argv) == 2):
        pass #with the file (in progress)
    else:
        return 1
    printBoard(board)
    solve(board)
    print("\n\n")
    printBoard(board)

if __name__ == '__main__':
  main(board_test)
