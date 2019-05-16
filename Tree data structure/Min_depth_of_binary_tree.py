# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

#  NOTE : The path has to end on a leaf node. 
# Example :

#          1
#         /
#        2
# min depth = 2.
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


def minDepth(A):
    if A==None:
        return 0
    if A.left ==None and A.right==None:
        return 1

    import sys
    l_depth = r_depth = sys.maxsize
    if A.left:
        l_depth = minDepth(A.left)
    if A.right:
        r_depth = minDepth(A.right)
    return min(l_depth,r_depth)+1

print(minDepth(createTree()))


