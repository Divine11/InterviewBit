def reverse(A):
    result = [0]*32
    counter = 31
    while A>0:
        result[counter] = A%2
        A = A//2
        counter -=1
    print(result)
    res = 0
    multiplication = [2**i for i in range(32)]
    for i in range(32):
        res += result[i]*multiplication[i]
    
    return res

reverse(0)
