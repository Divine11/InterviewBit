# Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

# Input:

# array of integers e.g {1, 2, 3}
#  NOTE: Solution will fit in a 32-bit signed integer 
# Example:

# [0, -1, 3, 100, 70, 50]

# => 70*50*100 = 350000
def maxp3(A):
    import sys
    inf = sys.maxsize
    max1 = max2 = max3 = -inf
    min1 = min2 = min3 = inf
    n = len(A)
    if n==2:
        return None
    for i in A:
        if i>max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i>max2:
            max3 = max2
            max2 = i
        elif i>max3:
            max3 = i
        if i<min1:
            min2 = min1
            min1 = i
        elif i<min2:
            min2 = i
    return max((max1*max2*max3),(max1*min1*min2))

print(maxp3([1, 3, 5, 2, 8, 0, -1, -3]))