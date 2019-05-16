# Given a binary tree, determine if it is height-balanced.

#  Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Example :

# Input : 
#           1
#          / \
#         2   3

# Return : True or 1 

# Input 2 : 
#          3
#         /
#        2
#       /
#      1

# Return : False or 0 
#          Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
#          Difference = 2 > 1. 
def getHeight(root):
    if root is None:
        return 0
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)
    return max(left_height,right_height)+1
def isBalanced(self,A):
    if A==None:
        return 1
    if abs(getHeight(A.left)-getHeight(A.right))<2 and isBalanced(A.left)==1 and isBalanced(A.right)==1:
        return 1
    return 0
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def createTree():
    root = TreeNode(100)
    root.left = TreeNode(98)
    root.right = TreeNode(102)
    root.left.left = TreeNode(96)
    root.left.right = TreeNode(99)
    root.left.left.right = TreeNode(97)
    root.left.left.left = TreeNode(95)
    return root
print(isBalanced("",createTree()))
