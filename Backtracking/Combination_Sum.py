# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The combinations themselves must be sorted in ascending order.
# CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
# The solution set must not contain duplicate combinations.
# Example, 
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:

# [2, 2, 3]
# [7]
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points. 
def combinationUtil(A,B,C,D):
    if B==0:
        D.append(C+[])
        return
    elif B<0:
        return
    for i in range(len(A)):
        C.append(A[i])
        combinationUtil(A[i:],B-A[i],C,D)
        C.pop()
def combinationSum(A,B):
    D = []
    A = list(set(A))
    A.sort()
    combinationUtil(A,B,[],D)
    return D

print(*combinationSum([8,10,6,11,1,16,8],28),sep ='\n')
