def prettyJSON(A):
    result = []
    indentation = 0
    temp = []
    i=0
    while i<len(A):
        if A[i]=='[' or A[i] =='{':
            if len(temp)!=0:
                result.append(("\t"*indentation)+''.join(temp))
                temp = []
            result.append(("\t"*indentation)+A[i])
            indentation +=1
            i+=1
        elif A[i]=='}' or A[i]==']':
            if len(temp)!=0:
                result.append(("\t"*indentation)+''.join(temp))
                temp =[]
            indentation -=1
            result.append(("\t"*indentation)+A[i])
            i+=1
        elif A[i]==',':
            if len(temp)==0:
                t = result[-1]
                t = t+A[i]
                result[-1] = t
                temp = []
                i+=1
            else:
                temp.append(A[i])
                result.append(("\t"*indentation)+''.join(temp))
                i+=1
                temp=[]
        else:
            temp.append(A[i])
            i+=1
    #return result
    print(*result,sep="\n")



print(prettyJSON('{A:"B",C:{D:"E",F:{G:"H",I:"J"}},K:L}'))


