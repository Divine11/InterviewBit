# Given a BST node, return the node which has value just greater than the given node.

# Example:

# Given the tree

#                100
#               /   \
#             98    102
#            /  \
#          96    99
#           \
#            97
# Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
# If there are no successor in the tree ( the value is the largest in the tree, return NULL).

# Using recursion is not allowed.

# Assume that the value is always present in the tree.
from Tree import TreeNode as T_Node
def getSuccessor(A,B):
    lis = []
    maxi = None
    if A.val>B:
        maxi = A
        if A.left:
            lis.append(A.left)
    else:
        if A.right:
            lis.append(A.right)
    while lis:
        temp = lis.pop()
        if temp.val>B:
            if maxi==None:
                maxi = temp
            elif temp.val<maxi.val:
                maxi = temp
            if temp.left:
                lis.append(temp.left)
        else:
            if temp.right:
                lis.append(temp.right)
    return maxi

def createTree():
    root = T_Node(100)
    root.left = T_Node(98)
    root.right = T_Node(102)
    root.left.left = T_Node(96)
    root.left.right = T_Node(99)
    root.left.left.right = T_Node(97)
    return root

root = createTree()
res = getSuccessor(root,97)
if res:
    print(res.val)
else:
    print(None)



