# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
# Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

# Example :

# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC"

#  Note:
# If there is no such window in S that covers all characters in T, return the empty string ''.
# If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
def minWindow(self, A, B):
    if(len(A)<len(B)):return ''
    if(A==B):return A
    mapp = {}
    for x in B:
        if x in mapp: mapp[x][1] += 1 
        else: mapp[x] = [0,1]
    winStart = 0
    winEnd = 0
    count = 0
    flag = 0
    mini  = A
    for winEnd in range(len(A)):
        if A[winEnd] in mapp:
            mapp[A[winEnd]][0]+=1
            if mapp[A[winEnd]][0]<=mapp[A[winEnd]][1]: count+=1
            if count==len(B):
                while(winStart<=winEnd):
                    if A[winStart] in mapp:
                        if mapp[A[winStart]][0]-1>=mapp[A[winStart]][1]:
                            mapp[A[winStart]][0] -= 1
                            winStart +=1
                        elif mapp[A[winStart]][0]-1==mapp[A[winStart]][1]-1:
                            if (winEnd+1-winStart)<len(mini): 
                                mini = A[winStart:winEnd+1]
                                flag=1
                            mapp[A[winStart]][0] -= 1
                            winStart+=1
                            count -= 1
                            break
                    else:winStart += 1
    if(flag==1):return mini
    else:return ''

print(minWindow("","ADOBECODEBANC","AABC"))



            




