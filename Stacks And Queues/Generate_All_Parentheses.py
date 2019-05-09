# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

def isValid(A):
    opening = ['(','{','[']
    closing = [')','}',']']
    res = []
    if A==None:
        return 1
    if len(A)==1:
        return 0
    for i in A:
        if i in opening:
            res.append(i)
        elif i in closing:
            ind = closing.index(i)
            if len(res)<1:
                return 0
            if res[-1]==opening[ind]:
                res.pop()
            else:
                return 0
        else:
            return 0
    if len(res)!=0:
        return 0
    return 1

print(isValid("{{"))
