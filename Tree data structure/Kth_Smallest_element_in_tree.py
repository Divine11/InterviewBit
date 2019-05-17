# Given a binary search tree, write a function to find the kth smallest element in the tree.

# Example :

# Input : 
#   2
#  / \
# 1   3

# and k = 2

# Return : 2

# As 2 is the second smallest element in the tree.
#  NOTE : You may assume 1 <= k <= Total number of nodes in BST 

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

def kthsmallest(self, A, B):
    res = inorderTraversal(A)
    return res[B-1]