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

def buildTree(A,B):
    if B:
        root = TreeNode(B[-1])
        idx = A.index(B[-1])
        root.right = buildTree(A[idx+1:],B[idx:-1:+1])
        root.left = buildTree(A[:idx+1],B[:idx])
        return root
B=[95, 97, 96, 99, 98, 103, 104, 102, 100]
A=[95, 96, 97, 98, 99, 100, 103, 102, 104]

root = buildTree(A,B)

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