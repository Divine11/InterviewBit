# Given a binary tree, flatten it to a linked list in-place.

# Example :
# Given


#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:

#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# Note that the left child of all nodes should be NULL.
def flatten(A):
    if A is None:
        return None
    left = flatten(A.left)
    right = flatten(A.right)
    if not left and not right:
        return A
    elif not left and right:
        return A
    elif left and not right:
        A.right = left
        A.left = None
        return A
    else:
        A.right = left
        cur = A
        while cur.right:
            cur = cur.right
        cur.right = right
        A.left = None
        return A
        
    
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
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    return root

def zigzagLevelOrder(A):
    print("yolo")
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
root = flatten(createTree())
print(zigzagLevelOrder(root))
