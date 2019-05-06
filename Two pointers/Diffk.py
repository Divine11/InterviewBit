def diffPossible(A,B):
    dic = {}
    for i in A:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1

    print(dic)
    
    for i in A:
        print(i,i-B,dic[i])
        if i-B in dic.keys():
            if i-B == i:
                if dic[i]>1:
                    return 1
            else:
                return 1
                
                
    return 0


print(diffPossible([ 1, 2, 2, 3, 4],0))
