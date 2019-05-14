# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

# The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.



# The input corresponding to the above configuration :

# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.

#  Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

def isValidSudoku(self, A):
    row_dic = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    col_dic = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    sub_box = {"00":[],"01":[],"02":[],"10":[],"11":[],"12":[],"20":[],"21":[],"22":[]}
    for i in range(9):
        row_dic[i] = [x for x in A[i] if x!='.']
        for j in range(9):
            if A[i][j]!='.':
                col_dic[j].append(A[i][j])
                sub_box[str(i//3)+str(j//3)].append(A[i][j])
    # print(row_dic)
    # print(col_dic)
    #print(sub_box)
    for i in range(9):
        if len(row_dic[i])!=len(set(row_dic[i])):
            #print("gaya","row",i)
            return 0
        if len(col_dic[i])!=len(set(col_dic[i])):
            #print("gaya","col",i)
            return 0
    for i in range(3):
        for j in range(3):
            #print(str(i)+str(j),len(sub_box[str(i)+str(j)]),len(set(sub_box[str(i)+str(j)])))
            if len(sub_box[str(i)+str(j)])!=len(set(sub_box[str(i)+str(j)])):
                return 0
    # for i in range():
    return 1
A = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
print(isValidSudoku("",A))
def printSoduko(A):
    for i in A:
        for j in i:
            print(j,end=' ')
        print()
#printSoduko(A)
