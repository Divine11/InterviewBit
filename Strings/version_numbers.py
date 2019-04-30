def compareVersion(A,B):
    i = 0
    equal = 0
    A_list = A.split('.')
    B_list = B.split('.')
    n = len(A_list)
    m = len(B_list)
    while i<m and i<n:
        tempa = A_list[i].lstrip('0')
        tempb = B_list[i].lstrip('0')
        if tempa!=tempb:
            if int(tempa)>int(tempb):
                return 1
            else:
                return -1
        i+=1
    
    while i<m:
        if B_list[i]>'0':
            return -1
        i+=1
    
    while i<n:
        if A_list[i]>'0':
            return 1
        i+=1

    return equal
    


print(compareVersion("02","2"))
    
