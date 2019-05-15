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

def preorderTraversal(A):
    cur = A
    res = []
    stack = []
    stack.append(A)
    while stack:
        temp = stack.pop()
        res.append(temp.val)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)
    return res

def pre(A):
    if A:
        print(A.val,end=" ")
        pre(A.left)
        pre(A.right)

print(preorderTraversal(createTree()))
pre(createTree())
            