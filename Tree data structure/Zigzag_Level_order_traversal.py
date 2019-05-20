# right to left for the next level and alternate between).

# Example : 
# Given binary tree

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return

# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]
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
            cur.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        else:
            if len(queue)>0:
                queue.append(None)
            if flag==1:
                cur = cur[::-1]
                res.append(cur+[])
                flag = 0
            else:
                res.append(cur+[])
                flag = 1
            cur = []
    return res

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
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

print(zigzagLevelOrder(createTree()))


