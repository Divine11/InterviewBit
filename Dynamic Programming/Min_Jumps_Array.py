# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example :
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# If it is not possible to reach the end index, return -1.
def jump(A):
    last = len(A) - 1
    jumps = 0
    reachable = 0      # reachable with current number of jumps 
    next_reachable = 0 # reachable with one additionnal jump
    for i, x in enumerate(A):
        
        if reachable >= last:
            break 
        
        if reachable < i:
            reachable = next_reachable
            jumps += 1
            if reachable < i:
                return -1
        next_reachable = max(next_reachable, i+x)
    
    return jumps