# You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.

# For this problem, return the indices of maximum continuous series of 1s in order.

# Example:

# Input : 
# Array = {1 1 0 1 1 0 0 1 1 1 } 
# M = 1

# Output : 
# [0, 1, 2, 3, 4] 

# If there are multiple possible solutions, return the sequence which has the minimum start index.
def maxone(arr,m):
    wL = wR = 0
    n = len(arr)
    # Left index and size of the widest window  
    bestL = bestWindow = 0
    
    # Count of zeroes in current window 
    zeroCount = 0
    
    # While right boundary of current  
    # window doesn't cross right end 
    while wR < n: 
            
        # If zero count of current window is less than m, 
        # widen the window toward right 
        if zeroCount <= m : 
            if arr[wR] == 0 : 
                zeroCount += 1
            wR += 1
    
        # If zero count of current window is more than m, 
        # reduce the window from left 
        if zeroCount > m : 
            if arr[wL] == 0 : 
                zeroCount -= 1
            wL += 1
    
        # Updqate widest window if 
        # this window size is more 
        if (wR-wL > bestWindow) and (zeroCount<=m) : 
            bestWindow = wR - wL 
            bestL = wL
        
    return [i for i in range(bestL,bestL+bestWindow)]

maxone([ 0, 1, 1, 1],0)
        
