# Given a binary tree, return a 2-D array with vertical order traversal of it.
# Go through the example and image for more details.

# Example :
# Given binary tree:

#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9
# returns

# [
#     [2],
#     [3],
#     [6 5],
#     [7],
#     [9]
# ]


# Note : If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
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

def verticalOrderTraversal(self,A):
    dic = {}
    stack = [[A,0]]
    while stack:
        temp,prio = stack.pop(0)
        if prio in dic:
            dic[prio].append(temp.val)
        else:
            dic[prio] = [temp.val]
        if temp.left:
            stack.append([temp.left,(prio-1)])
        if temp.right:
            stack.append([temp.right,(prio+1)])
    res = []
    ty = sorted(dic.keys())
    for i in ty:
        res.append(dic[i])
    return res

print(verticalOrderTraversal("",None))

