# Find the largest continuous sequence in a array which sums to zero.

# Example:


# Input:  {1 ,2 ,-2 ,4 ,-4}
# Output: {2 ,-2 ,4 ,-4}

#  NOTE : If there are multiple correct answers, return the sequence which occurs first in the array. 
def lszero(self, A):
    max_len = 0 
    n  = len(A)
    if A==None:
        return None
    if A==1:
        if A[0]==0:
            return [0]
        else:
            return None
    dic = {}
    sur_sum = 0
    start = 0
    end = 0
    diff=0
    for i in range(len(A)):
        sur_sum = sur_sum+A[i]
        if sur_sum==0:
            #print(i,start,end)
            if i+1>diff:
                start = -1
                end = i
                diff = end+1
            continue
        if sur_sum in dic:
            if i-dic[sur_sum]>diff:
                start = dic[sur_sum]
                end = i
                diff = end-start
        else:
            dic[sur_sum] = i
    #print(start,end)
    if sur_sum==0:
        return A
    return A[start+1:end+1]

print(lszero("",[-1, 20, 7, -22, 1, 21, 5, 24, -26, -16, -4, -9, 19, 8, -27, 28, 9, 8, -29, 29, 8, 9, 17, -28, 13, 20, -1, -8, -16 ]))