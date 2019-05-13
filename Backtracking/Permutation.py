# Given a collection of numbers, return all possible permutations.

# Example:

# [1,2,3] will have the following permutations:

# [1,2,3]
# [1,3,2]
# [2,1,3] 
# [2,3,1] 
# [3,1,2] 
# [3,2,1]
#  NOTE
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.

def permuteUtil(A,B,C):
    if len(A)==0:
        C.append(B+[])
        return 
    for i in range(len(A)):
        B.append(A[i])
        A.pop(i)
        permuteUtil(A,B,C)
        A.insert(i,B.pop())

def permute(A):
    C = []
    permuteUtil(A,[],C)
    return C


print(permute([1,2,3]))
