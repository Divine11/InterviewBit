class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def createTree():
    root = TreeNode(100)
    root.left = TreeNode(98)
    root.right = TreeNode(102)
    # root.left.left = TreeNode(96)
    # root.left.right = TreeNode(99)
    # root.left.left.right = TreeNode(97)
    # root.left.left.left = TreeNode(95)
    # root.right.left = TreeNode(103)
    # root.right.right = TreeNode(104)
    return root
def createTree2():
    root = TreeNode(100)
    root.left = TreeNode(102)
    root.right = TreeNode(98)

def is_mirror(A,B):
    if A is None and B is None: 
        return 1
    if A is None or B is None:
        return 0
    if (A is not None and B is not None): 
            if  A.val == A.val: 
                if (is_mirror(A.left, B.right)==1 and is_mirror(A.right, B.left)==1):
                    return 1 
  
    # If neither of the above conditions is true then root1 
    # and root2 are not mirror images 
    return 0

def isSymmetric(A):
    return is_mirror(A,A)

print(isSymmetric(createTree()))
    
