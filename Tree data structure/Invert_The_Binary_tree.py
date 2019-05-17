# Given a binary tree, invert the binary tree and return it. 
# Look at the example for more details.

# Example : 
# Given binary tree

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
# invert and return

#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4
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

def invertTree(A):
    if A is None:
        return A
    
    left = invertTree(A.left)
    right = invertTree(A.right)
    A.left = right
    A.right = left
    return A

def inorder(A):
    if A:
        inorder(A.left)
        print(A.val,end=" ")
        inorder(A.right)

root = createTree()
inorder(root)
root = invertTree(root)
print()
inorder(root)

