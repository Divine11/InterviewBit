# Given an inorder traversal of a cartesian tree, construct the tree.

#  Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 
#  Note: You may assume that duplicates do not exist in the tree. 
# Example :

# Input : [1 2 3]

# Return :   
#           3
#          /
#         2
#        /
#       1
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        res = str(self.val)
        return res
    def __repr__(self):
        return self.__str__()
        
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

def buildTree(A):
    if A:
        maxi = max(A)
        idx = A.index(maxi)
        root = TreeNode(maxi)
        root.left = buildTree(A[:idx])
        root.right = buildTree(A[idx+1:])
        return root

A = [4, 7, 5, 9, 6, 10, 3, 8, 2]
root = buildTree(A)
def zigzagLevelOrder(A):
    queue = []
    res = []
    cur = []
    if A is None:
        return res
    queue.append(A)
    queue.append(None)
    flag = 0
    while queue:
        temp = queue.pop(0)
        if temp:
            cur.append(temp)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        else:
            if len(queue)>0:
                queue.append(None)
            res.append(cur+[])
            cur = []
    return res

zigzagLevelOrder(root)

