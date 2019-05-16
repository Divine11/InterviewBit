# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers % 1003.

# Example :

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def createTree():
    root = TreeNode(1)
    root.left = TreeNode(3)
    return root
C = 0
def sumNumbersUtil(A,B):
    if A:
        if A.left==None and A.right==None:
            B+=str(A.val)
            global C
            B = B.lstrip('0')
            C+=int(B)
            C = C%1003
            return
        if A.left:
            sumNumbersUtil(A.left,B+str(A.val))
        if A.right:
            sumNumbersUtil(A.right,B+str(A.val))

def sumNumbers(A):
    sumNumbersUtil(A,"")
    return (C)

print(sumNumbers(createTree()))

