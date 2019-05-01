def divide(A,B):
    if A==B:
        return 1
    elif A<B:
        count = 0
        while A<B:
            A += A
            count +=1
        return count
    else:
        count = 0
        while B<A:
            B+=B
            count +=1
        return count

