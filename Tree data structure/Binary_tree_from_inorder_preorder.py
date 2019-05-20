# Given preorder and inorder traversal of a tree, construct the binary tree.

#  Note: You may assume that duplicates do not exist in the tree. 
# Example :

# Input :
#         Preorder : [1, 2, 3]
#         Inorder  : [2, 1, 3]

# Return :
#             1
#            / \
#           2   3

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

def getBinaryTree(A,B):
    if A:
        root = TreeNode(A[0])
        idx = B.index(A[0])
        root.left = getBinaryTree(A[1:idx + 1], B[:idx + 1])
        root.right = getBinaryTree(A[idx + 1:], B[idx + 1:])
        return root
    
A=[ 11, 14, 21, 20, 18, 28, 1, 10, 30, 26, 25, 8, 2, 4, 19, 27, 12, 6, 9, 23, 29, 17, 15, 31, 5, 16, 3, 24, 22, 13, 7 ]
B=[ 28, 1, 18, 10, 20, 30, 26, 25, 8, 2, 21, 4, 19, 14, 27, 11, 9, 23, 6, 17, 15, 29, 31, 12, 3, 16, 5, 24, 7, 13, 22 ]
root = getBinaryTree(A,B)

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


    