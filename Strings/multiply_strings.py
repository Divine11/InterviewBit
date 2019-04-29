def multiply(A,B):
    A = list(A)
    B = list(B)
    n1 = len(A)
    n2 = len(B)
    C = [0]*(n1+n2)
    i_n1 = 0
    i_n2 = 0
    for i in range(n1-1,-1,-1):
        a_digit = ord(A[i])-ord('0')
        carry = 0
        i_n2 = 0
        for j in range(n2-1,-1,-1):
            b_digit = ord(B[j])-ord('0')
            sum = a_digit*b_digit+C[i_n1+i_n2]+carry
            carry = sum//10
            C[i_n1+i_n2] = sum%10
            i_n2+=1
        if carry>0:
            C[i_n1+i_n2]+=carry
        i_n1+=1

    i = len(C)-1
    while i>=0 and C[i]==0:
        del C[i]
        i-=1
    C = C[::-1]
    #print(''.join([str(x) for x in C]))
    return ''.join([str(x) for x in C])
    

multiply("90","25")

