# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# Example :

# Given candidate set 10,1,2,7,6,1,5 and target 8,

# A solution set is:

# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]
def combinationUtil(A,B,C,D):
    if B==0:
        D[''.join([str(x) for x in C])] = C+[]
        return
    elif B<0:
        return
    for i in range(len(A)):
        C.append(A[i])
        combinationUtil(A[i+1:],B-A[i],C,D)
        C.pop()
def combinationSum(A,B):
    D = dict()
    A.sort()
    combinationUtil(A,B,[],D)
    return D.values()

print(*combinationSum([10,1,2,7,6,1,5],8),sep ='\n')
