# Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

# Note:

# 1) Return the indices `A1 B1 C1 D1`, so that 
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1 

# 2) If there are more than one solutions, 
#    then return the tuple of values which are lexicographical smallest. 

# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
# S2 : A2 B2 C2 D2

# S1 is lexicographically smaller than S2 iff
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR 
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
# Example:

# Input: [3, 4, 7, 1, 2, 9, 8]
# Output: [0, 2, 3, 5] (O index)
# If no solution is possible, return an empty list.
def equal(self, A):
    if len(A)<4:
        return []
    res = []
    dic = {}
    n = len(A)
    for i in range(n-1):
        for j in range(i+1,n):
            su = A[i]+A[j]
            if su in dic:
                dic[su].append([i,j])
            else:
                dic[su] = [[i,j]]
    for x in range(n-1):
        for y in range(x+1,n):
            n_su = A[x]+A[y]
            if n_su in dic:
                su = dic[n_su]
                #print(su)
                for k in su:
                    if k[0]>x and k[1]>x and k[1]!=y and k[1]!=x and k[0]!=y:
                        return [x,y,k[0],k[1]]
    return res
    

print(equal("",[1,1,1,1,1]))