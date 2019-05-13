# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Example :

# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Rain water trapped: Example 1

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.

def trap(A):
    n = len(A)
    left_greater_ele = [-1]
    stack = [A[0]]
    for i in range(1,n):
        while stack and stack[-1]<A[i]:
            stack.pop()
        if len(stack)==0:
            stack.append(A[i])
            left_greater_ele.append(-1)
        else:
            left_greater_ele.append(stack[-1])
        
    
   # print(left_greater_ele)
    right_greater_ele = [0]*n
    stack = [A[n-1]]
    right_greater_ele[-1] = -1
    for i in range(n-2,-1,-1):
        while stack and stack[-1]<A[i]:
            stack.pop()
        if len(stack)==0:
            stack.append(A[i])
            right_greater_ele[i] = -1
        else:
            right_greater_ele[i] = stack[-1]
        
    sum = 0
    for i in range(n):
        if left_greater_ele[i]==-1 or right_greater_ele[i]==-1:
            continue
        else:
            sum += min(left_greater_ele[i],right_greater_ele[i])-A[i]
    return sum

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

