# N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.

# Note : 0 represents the bulb is off and 1 represents the bulb is on.

# Example:

# Input : [0 1 0 1]
# Return : 4

# Explanation :
# 	press switch 0 : [1 0 1 0]
# 	press switch 1 : [1 1 0 1]
# 	press switch 2 : [1 1 1 0]
# 	press switch 3 : [1 1 1 1]
def bulbs(A):
    n = len(A)
    res = 0
    if n==0:
        return res
    if n==1:
        if A[0]==0:
            return 1
        else:
            return res
    start = -1
    end = -1
    current_state = 0
    i = 0
    while end<n:
        while i<n and A[i]!=current_state:
            i+=1
        if i==n:
            return res
        start = i
        while i<n and A[i]==current_state:
            i+=1
        end = i
        res+=1
        start = end
        current_state ^=1
    return res

print(bulbs([1,1,0,0,1,1,0,0,1]))