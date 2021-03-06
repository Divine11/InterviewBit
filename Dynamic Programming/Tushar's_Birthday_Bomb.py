# It’s Tushar’s birthday today and he has N friends. Friends are numbered [0, 1, 2, …., N-1] and i-th friend have a positive strength S(i). Today being his birthday, his friends have planned to give him birthday bombs (kicks :P). Tushar’s friends know Tushar’s pain bearing limit and would hit accordingly.
# If Tushar’s resistance is denoted by R (>=0) then find the lexicographically smallest order of friends to kick Tushar so that the cumulative kick strength (sum of the strengths of friends who kicks) doesn’t exceed his resistance capacity and total no. of kicks hit are maximum. Also note that each friend can kick unlimited number of times (If a friend hits x times, his strength will be counted x times)

# Note:

# Answer format = Vector of indexes of friends in the order in which they will hit.
# Answer should have the maximum no. of kicks that can be possibly hit. If two answer have the same no. of kicks, return one with the lexicographically smaller.
# [a1, a2, …., am] is lexicographically smaller than [b1, b2, .., bm] if a1 < b1 or (a1 = b1 and a2 < b2) … .
# Input cases are such that the length of the answer does not exceed 100000.
# Example:
# R = 11, S = [6,8,5,4,7]

# ans = [0,2]
# Here, [2,3], [2,2] or [3,3] also give the maximum no. kicks.
def solve(R,A):
    smallest = float('inf')
    k = 0
    for i in range(len(A)):
        if A[i] < smallest:
            smallest = A[i]
            k = i
    tolerance = R % smallest
    res = [k] * (R // smallest)
    i = 0
    j = 0
    while j < k and i < len(res):
        if A[j] - smallest <= tolerance:
            res[i] = j
            tolerance -= A[j] - smallest
            i+=1
        else:
            j+=1
    return res


print(solve(19,[18, 7, 6, 5, 4 ]))
