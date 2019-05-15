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

def postorderTraversal(A):
    cur = A
    res = []
    stack = [A]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res[::-1]

def post(A):
    if A:
        post(A.left)
        post(A.right)
        print(A.val,end=" ")
        
print(postorderTraversal(createTree()))
post(createTree())