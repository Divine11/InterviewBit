# Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example :

# Input : [2, 1, 2]
# Return  : 2 which occurs 2 times which is greater than 3/2. 
def majorityElement(A):
    majority_ele = A[0]
    count = 1
    for i in A[1:]:
        if i==majority_ele:
            count+=1
        else:
            count-=1
        if count==0:
            majority_ele = i
            count=1
    return majority_ele

majorityElement((2,3,2,4,2,5,5,2,2))