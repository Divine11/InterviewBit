# Find the intersection of two sorted arrays.
# OR in other words,
# Given 2 sorted arrays, find all the elements which occur in both the arrays.

def intersect(A,B):
    m  = len(A)
    n = len(B)
    i=j=0
    res = []
    while i<m and j<n:
        if A[i]==B[j]:
            res.append(A[i])
            i+=1
            j+=1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1
    return res