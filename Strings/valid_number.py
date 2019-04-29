def isNumber(A):
    A = A.lstrip(" ")
    A = A.rstrip(" ")
    temp = []
    if len(A)==0:
        return 0
    for i in range(len(A)):
        if ord('0')<= ord(A[i])<= ord('9') or A[i]=='.' or A[i]=='e' or A[i]=='-':
            if A[i]=='-':
                if len(temp)!=0 and temp[-1]!='e':
                    return 0
                if i==len(A)-1:
                    return 0
            if A[i]=='e':
                if i==len(A)-1:
                    return 0
                if i==0:
                    return 0
                if '.' in temp:
                    return 0
            if A[i]=='.':
                if i==len(A)-1:
                    return 0
                if i==0:
                    return 0
                if 'e' in temp:
                    return 0
            temp.append(A[i])
        else:
            return 0 
    return 1
