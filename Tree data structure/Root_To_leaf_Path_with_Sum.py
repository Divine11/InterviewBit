# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
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

def pathSumUtil(A,Su,B,C):
    if A:
        #print("we are at ",A.val,B)
        if Su-A.val==0 and A.left==None and A.right==None:
            C.append(B+[A.val])
            return
        if A.left:
            B.append(A.val)
            pathSumUtil(A.left,Su-A.val,B,C)
            B.pop()
        if A.right:
            B.append(A.val)
            pathSumUtil(A.right,Su-A.val,B,C)
            B.pop()

def pathSum(A, B):
    C =[]
    pathSumUtil(A,B,[],C)
    return C

print(pathSum(createTree(),297))