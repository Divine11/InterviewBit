def merge(A,B):
    m = len(A)
    n = len(B)
    i=j=k=0
    C = [None]*(m+n)
    while i<m and j<n:
        if A[i]<B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            j+=1
        k+=1
    
    while i<m:
        C[k] = A[i]
        k+=1
        i+=1
    while j<m:
        C[k] = B[j]
        k+=1
        j+=1
    return C


