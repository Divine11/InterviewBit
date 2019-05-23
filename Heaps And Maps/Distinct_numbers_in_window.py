# You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of distinct numbers in all windows of size K.

# Formally, return an array of size N-K+1 where i’th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.

# Note:

# If K > N, return empty array.
# For example,

# A=[1, 2, 1, 3, 4, 3] and K = 3

# All windows of size K are

# [1, 2, 1]
# [2, 1, 3]
# [1, 3, 4]
# [3, 4, 3]

# So, we return an array [2, 3, 3, 2].
def dNums(A, B):
    res = []
    n = len(A)
    if B>n:
        return res
    if B==1:
        res = [1]*(n-B+1)
        return res
    dic = {}
    for i in A[:B]:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    count = len(dic)
    res.append(count)
    for i in range(1,n-B+1):
        # print("we are at ",i," array is ",A[i:i+B]," dic is ",dic)
        subtract = A[i-1]
        addition = A[i+B-1]
        if subtract==addition:
            res.append(count)
            continue
        dic[subtract]-=1
        if addition in dic:
            if dic[addition]==0:
                count+=1
            dic[addition]+=1
        else:
            dic[addition]=1
            count+=1
        if dic[subtract]<1:
            count-=1
            dic[subtract]=0
        res.append(count)
    return res
    
print(dNums([80, 18, 80, 80, 80, 80, 80, 80, 94, 18],8))