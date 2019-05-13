# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# There might be multiple gray code sequences possible for a given n.
# Return any such sequence.
def bin_to_int(arr):
    k = 0
    num = 0
    for i in range(len(arr)-1,-1,-1):
        num += 2**k * arr[i]
        k=k+1
    return num
def grayUtil(A,B,zero,one,C):
    #print("In starting",A,B)
    if len(B)==A:
        C.append(bin_to_int(B+[]))
        return
    else:
        if zero<A:
            B.append(0)
            grayUtil(A,B,zero+1,one,C)
            B.pop()
        if one<A:
            B.append(1)
            grayUtil(A,B,zero,one+1,C)
            B.pop()
    #print("end",A,B)

def grayCode(A):
    C = []
    grayUtil(A,[],0,0,C)
    return C


print(grayCode(10))

