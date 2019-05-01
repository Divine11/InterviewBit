def findMinXor(A):
    A.sort()
    import sys
    min = sys.maxsize
    for i in range(0,len(A)-1):
        if A[i]^A[i+1]<min:
            min = A[i]^A[i+1]

    return min

print(findMinXor([0,4,7,9]))
