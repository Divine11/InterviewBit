# Given a string S, reverse the string using stack.

# Example :

# Input : "abc"
# Return "cba"

def reverseString(A):
    #print("We are in the beginning ",A)
    if len(A)<2:
        #print("Length is smaller then 2 else returning")
        return A
    
    rev = reverseString(A[1:])
    #print("A is ",A," rev is ",rev," A[0] is ",A[0])
    return rev+A[0]

print(reverseString("abcdef"))