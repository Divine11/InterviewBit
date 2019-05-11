# Given a set of distinct integers, S, return all possible subsets.

#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The list is not necessarily sorted.
# Example :

# If S = [1,2,3], a solution is:

# [
#   [],
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 3],
#   [2],
#   [2, 3],
#   [3],
# ]

def subsetUtil(A,B,C):
    C.append(B+[])
    if len(A)==0: 
        return
    for i in range(len(A)):
        B.append(A[i])
        subsetUtil(A[i+1:],B,C)
        B.pop()
    
        


def subsets(A):
    B = []
    C = []
    A.sort()
    subsetUtil(A,B,C)
    print(C)

subsets([1,2,3])
