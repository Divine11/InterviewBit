# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

# More formally,

# G[i] for an element A[i] = an element A[j] such that 
#     j is maximum possible AND 
#     j < i AND
#     A[j] < A[i]
# Elements for which no smaller element exist, consider next smaller element as -1.

# Example:

# Input : A : [4, 5, 2, 10, 8]
# Return : [-1, 4, -1, 2, 2]

# Example 2:

# Input : A : [3, 2, 1]
# Return : [-1, -1, -1]

def prevSmaller(A):
    if A==None:
        return A
    if len(A)==1:
        return [-1]
    else:
        stack = []
        for i in range(len(A)):
            if len(stack)==0:
                stack.append(A[i])
                A[i] = -1
            else:
                #print(stack,A[i])
                while stack and stack[-1]>=A[i]:
                    stack.pop()
                #print(stack)
                if len(stack)==0:
                    stack.append(A[i])
                    A[i]=-1
                else:
                    stack.append(A[i])
                    A[i] = stack[-2]
                #print(stack,A[i])
        print(A)

prevSmaller([39, 27, 11, 4, 24, 32, 32, 1 ]) 