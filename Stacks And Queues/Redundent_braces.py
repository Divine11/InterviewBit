# Write a program to validate if the input string has redundant braces?
# Return 0/1

# 0 -> NO
# 1 -> YES
# Input will be always a valid expression

# and operators allowed are only + , * , - , /

# Example:

# ((a + b)) has redundant braces so answer will be 1
# (a + (a + b)) doesn't have have any redundant braces so answer will be 0

def braces(A):
    res = []
    if A==None:
        return 0
    if len(A)==1:
        if A[0]!='(':
            return 0
        else:
            return 1
    for i in A:
        #print('starting i =',i,' res is ',*res)
        if i ==')':
            count = 0
            c = res.pop()
            while len(res)!=0 and c!='(':
                if c=='+' or c=='*' or c=='-' or c=='/':
                    count+=1
                c = res.pop()
            if count==0:
                return 1
        else:
            res.append(i)
        #print('ending i =',i,' res is ',*res)
    return 0

print(braces("(a+(b+c))"))