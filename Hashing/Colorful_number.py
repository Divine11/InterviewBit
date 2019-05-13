# For Given Number N find if its COLORFUL number or not

# Return 0/1

# COLORFUL number:

# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
# Example:

# N = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

# Output : 1
def break_into_list(A):
    result = []
    temp = A
    while temp>0:
        result.append(temp%10)
        temp //= 10
    
    result = result[::-1]
    return result

def colorful(self, A):
    dic = {}
    lis = break_into_list(A)
    n = len(lis)
    if n<2:
        return 1
    row = [0]*n
    counter = 0
    prev = 1
    for i in range(1):
        for j in range(n):
            row[counter] = prev*lis[j]
            dic[row[counter]] = 1
            prev = row[counter]
            counter += 1
    for i in range(1,n):
        for j in range(i,n):
            if lis[i-1]==0:
                continue
            row[j] = row[j]//lis[i-1]
            dic[row[j]] = 1
    print(dic)
    if len(dic.items())==(n*(n+1)//2):
        return 1
    return 0

print(colorful("",100))