# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Example :

# Input : 
#    1
#   /  \
#  2    3

# Output : 0 or False


# Input : 
#   2
#  / \
# 1   3

# Output : 1 or True 
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def isValidBstUtil(A,maxi,mini):
    if A==None:
        return 1
    if A.val<mini:
        return 0
    elif A.val>maxi:
        return 0
    return isValidBstUtil(A.left,A.val,mini) and isValidBstUtil(A.right,maxi,A.val)
def isValidBST(self, A):
    import sys
    return isValidBstUtil(A,sys.maxsize,-sys.maxsize)
def createTree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)
    root.left.left.right = TreeNode(97)
    return root

root = createTree()
print(isValidBST("",root))
    
