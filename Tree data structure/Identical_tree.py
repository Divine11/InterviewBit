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

def is_identical(A,B):
    if A==None and B==None:
        return 1
    elif A==None or B==None:
        return 0
    else:
        if (A.val==B.val and is_identical(A.left,B.left) and is_identical(A.right,B.right)):
            return 1
        return 0

print(is_identical(createTree(),createTree()))
    