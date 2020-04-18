###########################################
#
# This is a sudoku solver in python.
#
# Author : Antoine-Alexis Bourdon
# Link : https://github.com/antoinealexisb/sudoku_solver
# Version : 0.1.3
# Year : 2020-04
# Dependency : sys
#
###########################################

import sys

'''The function use recursion to find the right value in board
Arguments:
    --board : Array(board of sudoku)
Return:
    - : boolean (True = board correctly, False = not correctly)
'''
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
    print("\n")
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
    if (len(boardMain) != 81):
        print("Error : You have not copied your grid board correctly.")
    tmp=[]
    for i in range(9):
        tmp.append([])
        for j in range(9):
            tmp[i].append(int(boardMain[i*9+j]))
    return tmp

'''Function that loads the grid board file.
Arguments :
    -file : the file specified in the command
Return :
    - board : (the generated board)
'''
def charger(file):
    print("\n ---- Filename : ",file)
    try:
        text_file = open(file, "r")
    except:
        print("Error, File Not found ! : ", file)
        exit(1)
    tmp = text_file.readlines()
    if (len(tmp) != 9):
        print("Error : Your board does not contain 9 lines")
        exit(1)
    if (len(tmp[0]) != 18):
        print("Error : Your board does not contain 9 colomns")
        exit(1)
    return "".join(tmp).replace(" ", "").replace("\n","")



def main():
    '''Main function.
    '''
    if (len(sys.argv) == 1 ):
        boardMain = str(input("Give your sudoku board :"))
    elif (len(sys.argv) == 2):
        boardMain = charger(sys.argv[1])
    else:
        return 1
    board = substitution(boardMain)
    printBoard(board)
    solve(board)
    printBoard(board)

if __name__ == '__main__':
  main()
