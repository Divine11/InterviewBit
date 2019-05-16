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

def getBST(arr):
    if len(arr)==0:
        return None
    elif len(arr)==1:
        return TreeNode(arr[0])
    else:
        n = len(arr)
        root = TreeNode(arr[n//2])
        root.left = getBST(arr[:n//2])
        root.right = getBST(arr[n//2+1:])
        return root
    
def inorderTraversal(A):
    stack = []
    cur = A
    while cur!=None:
        stack.append(cur)
        cur = cur.left
    res = []
    #print(stack)
    while stack:
        temp = stack.pop()
        #print("we are currently at ",temp.val)
        res.append(temp.val)
        if temp.right:
            cur = temp.right
            stack.append(temp.right)
            while cur.left:
                #print("Pushing",cur.left.val)
                stack.append(cur.left)
                cur= cur.left
            
    return res

print(inorderTraversal(getBST([5,6,7,8,9,10,11,12,13])))

