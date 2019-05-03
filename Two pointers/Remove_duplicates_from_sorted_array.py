# Remove duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

# Note that even though we want you to return the new length, make sure to change the original array as well in place

# Do not allocate extra space for another array, you must do this in place with constant memory.

#  Example: 
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2]. 
def removeDuplicates(A):
    if len(A)<=1:
        return len(A)
    slot = 1
    prev = A[0]
    count = 1
    for i in range(1,len(A)):
        if prev!=A[i]:
            A[slot] = A[i]
            slot+=1
            prev= A[i]
            count = 1
        else:
            count+=1
            if count<3:
                A[slot] = A[i]
                slot+=1
                prev = A[i]
            else:
                prev = A[i]
    return slot

A = [1,2,2,3,3,3,3,4,5,5]
print(removeDuplicates(A))
print(A)