# Given a binary tree

#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

#  Note:
# You may only use constant extra space.
# Example :

# Given the following binary tree,

#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:

#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
#  Note 1: that using recursion has memory overhea
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    def __str__(self):
        next = None
        if self.next:
            next = self.next.val
        res = str(self.val)+"->"+str(next)
        return res
    def __repr__(self):
        return self.__str__()

def createTree():
    root = TreeLinkNode(100)
    root.left = TreeLinkNode(98)
    root.right = TreeLinkNode(102)
    root.left.left = TreeLinkNode(96)
    root.left.right = TreeLinkNode(99)
    root.left.left.right = TreeLinkNode(97)
    root.left.left.left = TreeLinkNode(95)
    root.right.left = TreeLinkNode(103)
    root.right.right = TreeLinkNode(104)
    return root

def connect(root):
    if root is None:
        return root
    queue = [root,None]
    while queue:
        current = queue.pop(0)
        while current:
            next = queue.pop(0)
            current.next = next
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            current = next
        if len(queue)>0:
            queue.append(None)
    return root

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
    

    
root = connect(createTree())
zigzagLevelOrder(root)