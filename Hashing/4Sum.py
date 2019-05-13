# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

#  Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
# Example : 
# Given array S = {1 0 -1 0 -2 2}, and target = 0
# A solution set is:

#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
#     (-1,  0, 0, 1)
# Also make sure that the solution set is lexicographically sorted.
# Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])

def fourSum(self, A, B):
    res = set()
    store = dict()
    if not A or len(A)==0:
        return list(res)
    A.sort()
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            curSum = A[i]+A[j]
            if (B-curSum) in store:
                for f, s in store[B-curSum]:
                    if i>s:
                        res.add((A[f], A[s], A[i], A[j]))
            if (curSum) not in store:
                store[curSum] = [(i, j)]
            else:
                store[curSum].append((i, j))
    res = list(res)
    res.sort()
    return res
    


print(fourSum("",[1,1,2,-1,1,-1],0))
