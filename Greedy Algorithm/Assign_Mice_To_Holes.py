# There are N Mice and N holes are placed in a straight line. 
# Each hole can accomodate only 1 mouse. 
# A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.
# Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

# Example:

# positions of mice are:
# 4 -4 2
# positions of holes are:
# 4 0 5

# Assign mouse at position x=4 to hole at position x=4 : Time taken is 0 minutes 
# Assign mouse at position x=-4 to hole at position x=0 : Time taken is 4 minutes 
# Assign mouse at position x=2 to hole at position x=5 : Time taken is 3 minutes 
# After 4 minutes all of the mice are in the holes.

# Since, there is no combination possible where the last mouse's time is less than 4, 
# answer = 4.
# Input:

# A :  list of positions of mice
# B :  list of positions of holes
# Output:

# single integer value
#  NOTE: The final answer will fit in a 32 bit signed integer. 
def mice(A,B):
    n = len(A)
    A.sort()
    B.sort()
    diff = 0
    #print(new_A)
    for i in range(n):
        if diff<abs(A[i]-B[i]):
            diff = abs(A[i]-B[i])
    return diff

print(mice([90, -96, -60, 77, 65, 38, -13, -11, 46, 82, 71, -78, -5, 42, 90, 84, -44, -10, -2],[61, 92, 58, 90, -59, 2, -13, -49, 24, 76, -72, -55, -22, -73, 47, -33, -70, 82, -84 ]))