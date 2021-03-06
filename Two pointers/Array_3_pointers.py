# You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

# **abs(x) is absolute value of x and is implemented in the following manner : **

#       if (x < 0) return -x;
#       else return x;
# Example :

# Input : 
#         A : [1, 4, 10]
#         B : [2, 15, 20]
#         C : [10, 12]

# Output : 5 
#          With 10 from A, 15 from B and 10 from C

def calculate_value(a,b,c):
    return max(abs(a-b),abs(b-c),abs(c-a))

def minimize(A,B,C):
    import sys
    mini = sys.maxsize
    n = len(A)
    m = len(B)
    o = len(C)
    i=j=k=0
    while i<n and j<m and k<o:
        value = calculate_value(A[i],B[j],C[k])
        if value<mini:
            mini = value
        min_value = min(A[i],B[j],C[k])
        if min_value==A[i]:
            i+=1
        elif min_value == B[j]:
            j+=1
        else:
            k+=1
    return mini

A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]

print(minimize(A,B,C))


