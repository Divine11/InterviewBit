# Given a number N, return number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
# Two ways are different if there exists a chord which is present in one way and not in other.

# For example,

# N=2
# If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
# {(1-2), (3-4)} and {(1-4), (2-3)}

# So, we return 2.
# Notes:

# 1 ≤ N ≤ 1000
# Return answer modulo 109+7.
def chordCnt(self, A):
    MODU = 10**9 + 7
    dp = [0] * (A+1)
    dp[0] = 1
    for n in range(1, A+1):
        res = 0
        for i in range(n):
            res += dp[i] * dp[n-1-i]
            res %= MODU
        dp[n] = res
        
    return dp[A]