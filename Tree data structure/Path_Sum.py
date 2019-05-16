# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Example :

# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
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
    root.right.left = TreeNode(103)
    root.right.right = TreeNode(104)
    return root

def hasPathSumUtil(A,B):
    if A:
        #print("we are at ",A.val,B)
        if B-A.val==0 and A.left==None and A.right==None:
            return 1
        if hasPathSumUtil(A.left,B-A.val)==1 or hasPathSumUtil(A.right,B-A.val)==1:
            return 1
    return 0


def hasPathSum(A, B):
    return hasPathSumUtil(A,B)

print(hasPathSum(createTree(),297))
