# Given a string s, partition s such that every string of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

#   [
#     ["a","a","b"]
#     ["aa","b"],
#   ]
#  Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
# *
# *
# *
# (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
# In the given example,
# ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
def isPalindrome(str):
    return str==str[::-1]
def partitionUtil(A,B,C):
    if len(A)==0:
        C.append(B+[])
        return
    temp = ""
    for i in range(len(A)):
        temp += A[i]
        if(isPalindrome(temp)):
            B.append(temp)
            partitionUtil(A[i+1:],B,C)
            B.pop()

def partition(A):
    C = []
    partitionUtil(A,[],C)
    return C

partition("aabc")
