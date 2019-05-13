# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# N Queens: Example 1

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
def isSafe(board, row, col,A): 

    for i in range(col): 
        if board[row][i] == 'Q': 
            return False
  
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
        if board[i][j] == 'Q': 
            return False

    for i,j in zip(range(row,A,1), range(col,-1,-1)): 
        if board[i][j] == 'Q': 
            return False
  
    return True
  
def solveNQUtil(board, col,A,res): 
    # base case: If all queens are placed 
    # then return true 
    if col >= A:
        res.append([''.join(x) for x in board])
        return True
  
    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(A): 
  
        if isSafe(board, i, col,A): 
            # Place this queen in board[i][col] 
            board[i][col] = 'Q'
  
            # recur to place rest of the queens 
            if solveNQUtil(board, col+1,A,res) == True: 
                return True
  
            # If placing queen in board[i][col 
            # doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = '.'
  
    # if the queen can not be placed in any row in 
    # this colum col  then return false 
    return False
def solveNQueens(A):
    res = []
    for i in range(A//2):
        board = [[ '.' for i in range(A) ] for j in range(A)]
        solveNQUtil(board,i,A,res)
    return res

solveNQueens(4)
