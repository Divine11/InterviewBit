def what_we_want_to_minimize(a,b,c):
    return abs(max(a,b,c)-min(a,b,c))


def solve(A,B,C):
    a = len(A)
    b = len(B)
    c = len(C)
    i=j=k=0
    import sys
    mini = sys.maxsize
    while i<a and j<b and k<c:
        if what_we_want_to_minimize(A[i],B[j],C[k])<mini:
            mini = what_we_want_to_minimize(A[i],B[j],C[k])
        if min(A[i],B[j],C[k])==A[i]:
            i+=1
        elif min(A[i],B[j],C[k])==B[j]:
            j+=1
        else:
            k+=1
    return mini