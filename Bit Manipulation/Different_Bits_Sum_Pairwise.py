def sum_difference_bit_pairwise(arr,n):
    result = 0
    for i in range(0,32):
        count = 0
        for j in arr:
            if j&(1<<i)>0:
                count +=1
        result += (count*(n-count)*2)
        result = result%(1000000007)
    return result

print(sum_difference_bit_pairwise([1,3,5],3))
