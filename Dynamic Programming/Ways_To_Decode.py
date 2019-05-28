# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# Example :

# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

def numDecodings(A):
    n = len(A)
    if n==0:
        return 0
    if n==1:
        if A=="0":
            return 0
        return 1
    res = [0]*n
    res[0] = 1
    if A=="10":
        return 1
    for i in range(1,n):
        if A[i]=='0' and A[i-1]=='0':
            return 0
        if A[i]!='0':
            res[i] = res[i-1]
        if A[i-1]=='0' and A[i-2]>'2' and i-2>=0:
            return 0
        if int(A[i-1]+A[i])<=26 and i-2>=0:
            res[i]+= res[i-2]
        #print(res)
    return res[-1]

numDecodings("32925665678138257423442343752148360796465852883409126159293254159974370974059818198867156827877059067081419274873853679038")