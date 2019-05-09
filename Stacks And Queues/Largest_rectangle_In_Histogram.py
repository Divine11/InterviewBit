# Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Largest Rectangle in Histogram: Example 1

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# Largest Rectangle in Histogram: Example 2

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
def largestRectangleArea(A):
    stack = list() 
  
    max_area = 0 # Initalize max area 
  
    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(A): 
          
        # If this bar is higher  
        # than the bar on top 
        # stack, push it to stack 
  
        if (not stack) or (A[stack[-1]] <= A[index]): 
            stack.append(index) 
            index += 1
  
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with  
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for  
        # the top and element before top in stack 
        # is 'left index' 
        else: 
            # pop the top 
            top_of_stack = stack.pop() 
  
            # Calculate the area with  
            # histogram[top_of_stack] stack 
            # as smallest bar 
            area = (A[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
  
            # update max area, if needed 
            max_area = max(max_area, area) 
  
    # Now pop the remaining bars from  
    # stack and calculate area with  
    # every popped bar as the smallest bar 
    while stack: 
          
        # pop the top 
        top_of_stack = stack.pop() 
  
        # Calculate the area with  
        # histogram[top_of_stack]  
        # stack as smallest bar 
        area = (A[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
  
        # update max area, if needed 
        max_area = max(max_area, area) 
  
    # Return maximum area under  
    # the given histogram 
    return max_area 


print(largestRectangleArea([2,0,1]))