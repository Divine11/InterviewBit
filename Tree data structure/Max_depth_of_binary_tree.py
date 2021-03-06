# Given a binary tree, find its maximum depth.

# The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

#  NOTE : The path has to end on a leaf node. 
# Example :

#          1
#         /
#        2
# max depth = 2.
def maxDepth(A):
    if A==None:
        return 0
    
    l_depth = maxDepth(A.left)
    r_depth = maxDepth(A.right)

    return 1 + max(l_depth,r_depth)