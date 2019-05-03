# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
def threeSum(self, A):
    A.sort()
    n=len(A)
    dic = {}
    for i in range(0,n-2):
        l = i+1
        r= n-1
        while l<r:
            if A[l]+A[r]+A[i]==0:
                if (str(A[i])+str(A[l])+str(A[r])) not in dic.keys():
                    dic[(str(A[i])+str(A[l])+str(A[r]))] = [A[i],A[l],A[r]]
                l+=1
                r-=1
            elif A[l]+A[r]+A[i]<0:
                l+=1
            else:
                r-=1
    return dic.items()