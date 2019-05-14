# Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

# Example :

# Input :

# A : [1 5 3]
# k : 2
# Output :

# 1
# as 3 - 1 = 2

# Return 0 / 1 for this problem.

def diffPossible(self, A, B):
    mapp={}
    for x in A:
        if mapp.get(x+B,False)==True or mapp.get(x-B,False)==True:
            return 1
        mapp[x]=True
    return 0

print(diffPossible("",[34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29],97))
