# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers.

# Assume that there will only be one solution

# Example: 
# given array S = {-1 2 1 -4}, 
# and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
def threeSumClosest(A,B):
    A.sort()
    import sys
    distance = sys.maxsize
    su = sys.maxsize
    n = len(A)
    print(A)
    for i in range(0,n-2):
        l = i+1
        r = n-1
        while l<r:
            print(distance,A[i],A[l],A[r],i,l,r)
            if abs(abs(sum([A[i],A[l],A[r]]))-abs(B))<distance:
                distance = abs(abs(sum([A[i],A[l],A[r]]))-abs(B))
                su = sum([A[i],A[l],A[r]])
            elif sum([A[i],A[l],A[r]])>B:
                r-=1
            else:
                l+=1
    return su

print(threeSumClosest([ 5, -2, -1, -10, 10 ],5))

