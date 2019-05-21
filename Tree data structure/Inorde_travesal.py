# Given a binary tree, return the inorder traversal of its nodes’ values.

# Example :
# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def createTree():
    root = TreeNode(10)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.left.left.right = TreeNode(5)
    root.left.left.left = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(2)
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

print(inorderTraversal(createTree()))

