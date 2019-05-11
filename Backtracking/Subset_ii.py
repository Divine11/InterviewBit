# Given a collection of integers that might contain duplicates, S, return all possible subsets.

#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# Example :
# If S = [1,2,2], the solution is:

# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]
def subsetUtil(A,B,C):
    C[''.join([str(x) for x in B])] = B+[]
    if len(A)==0: 
        return
    for i in range(len(A)):
        B.append(A[i])
        subsetUtil(A[i+1:],B,C)
        B.pop()
    
        


def subsetsWithDup(A):
    B = []
    C = dict()
    A.sort()
    subsetUtil(A,B,C)
    return C.values()

print(*subsetsWithDup([6, 6, 3, 3, 6, 5 ]),sep='\n')
