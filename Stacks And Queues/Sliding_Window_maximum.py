# A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window. The following example will give you more clarity.

# Example :

# The array is [1 3 -1 -3 5 3 6 7], and w is 3.

# Window position	Max
 	 
# [1 3 -1] -3 5 3 6 7	3
# 1 [3 -1 -3] 5 3 6 7	3
# 1 3 [-1 -3 5] 3 6 7	5
# 1 3 -1 [-3 5 3] 6 7	5
# 1 3 -1 -3 [5 3 6] 7	6
# 1 3 -1 -3 5 [3 6 7]	7
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]

#  Note: If w > length of the array, return 1 element with the max of the array. 
# Seen this question in a real interview before

def slidingMaximum(A,B):
    n = len(A)
    if n==0:
        return None
    if n<2 or B>=n:
        return [max(A)]
    max_upto=[0 for i in range(n)] 
  
    res = []
    # Update max_upto array similar to 
    # finding next greater element 
    s=[] 
    s.append(0) 
  
    for i in range(1,n): 
        while (len(s) > 0 and A[s[-1]] < A[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1] 
          
        s.append(i) 
  
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
  
    j = 0
    for i in range(n - B + 1): 
  
        # j < i is to check whether the 
        # jth element is outside the window 
        while (j < i or max_upto[j] < i + B - 1): 
            j += 1
        res.append(A[j])
    return res

print(slidingMaximum([1],1))
