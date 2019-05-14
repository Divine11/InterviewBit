# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

# Make sure the combinations are sorted.

# To elaborate,

# Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# Entries should be sorted within themselves.
# Example :
# If n = 4 and k = 2, a solution is:

# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points. 
def combineUtil(A,B,C,D,E):
    if B==0:
        E.append(C+[])
        return
    for i in range(D,A+1):
        C.append(i)
        combineUtil(A,B-1,C,i+1,E)
        C.pop()
def combine(A,B):
    E = []
    combineUtil(A,B,[],1,E)
    return E

print(combine(4,3))