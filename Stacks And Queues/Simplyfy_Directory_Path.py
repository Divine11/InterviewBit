# Given an absolute path for a file (Unix-style), simplify it.

# Examples:

# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Note that absolute path always begin with ‘/’ ( root directory )
# Path will not have whitespace characters.
def simplifyPath(A):
    res = []
    if A==None:
        return '/'
    div = A.split('/')
    for i in div:
        if len(i)==0 or i=='.':
            continue
        elif i=='..':
            if len(res)>0:
                res.pop()
        else:
            res.append(i)
    
    return '/'+'/'.join(res)


simplifyPath("/a//////b///////a/////")