# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example :

# Input : 3
# Return : 3

# Steps : [1 1 1], [1 2], [2 1]
def climbStairs(A):
    if A==0:
        return 0
    if A==1:
        return 1
    if A==2:
        return 2
    res = [0]*A
    res[0] = 1
    res[1] = 2
    i = 2
    while i<A:
        res[i] = res[i-1]+res[i-2]
        i+=1
    return res[-1]

climbStairs(6)