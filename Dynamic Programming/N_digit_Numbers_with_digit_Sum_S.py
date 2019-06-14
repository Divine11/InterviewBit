# Find out the number of N digit numbers, whose digits on being added equals to a given number S. Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.
#
# Since the answer can be large, output answer modulo 1000000007
#
# **
#
# N = 2, S = 4
# Valid numbers are {22, 31, 13, 40}
# Hence output 4.
def solve(A,B):
    table = [[0 for i in range(B+1)] for j in range(A+1)]
    table[1] = [1]*(B+1)
    for i in range(2,A+1):
        for j in range(1,B+1):
            table[i][j] = (table[i-1][j]+table[i][j-1])%1000000007
    #print(table)
    return table[A][B]

A = int(input())
B = int(input())
print(solve(A,B))