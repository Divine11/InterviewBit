# Given a string, 
# find the length of the longest substring without repeating characters.

# Example:

# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

# For "bbbbb" the longest substring is "b", with the length of 1.
def lengthOfLongestSubstring(self, A):
    n = len(A)
    if n==0:
        return 0
    if n==1:
        return 1
    start = 0
    end = 0
    cur_len = 0
    max_len = 0
    current = 0
    dic = {}
    while current <n:
        print("At starting",dic,current,start,cur_len)
        if A[current] not in dic:
            dic[A[current]] = 1
            cur_len+=1
            current+=1
        else:
            del dic[A[start]]
            start+=1
            cur_len-=1
        if cur_len>max_len:
            max_len = cur_len
        print("At End",dic,current,start,cur_len)
    return max_len

print(lengthOfLongestSubstring("","the pot is full"))


