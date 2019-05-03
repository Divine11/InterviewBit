# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: Using library sort function is not allowed.

def countingSort(arr):
    #here we know the range
    counting_array = [0]*3
    for i in arr:
        counting_array[i] += 1
    for i in range(1,3):
        counting_array[i] += counting_array[i-1]
    #print(counting_array)
    result = [None]*len(arr)
    for i in arr:
        #print(i,counting_array[i])
        result[counting_array[i]-1] = i
        counting_array[i] -= 1
    return result

def sortColors(A):
    return countingSort(A)

print(sortColors([0,1,2,2,1,1,2,0,2,1,2]))
    