# Recover Binary Search Tree
# Asked in:  
# Microsoft
# Amazon
# Two elements of a binary search tree (BST) are swapped by mistake.
# Tell us the 2 values swapping which the tree will be restored.

#  Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution? 
# Example :


# Input : 
#          1
#         / \
#        2   3

# Output : 
#        [1, 2]

# Explanation : Swapping 1 and 2 will change the BST to be 
#          2
#         / \
#        1   3
# which is a valid BST 
# 
def recoverTree(self, A):
    self.first = None
    self.prev = None
    self.last = None
    self.traverse(A)
    return([self.last, self.first])
    
def traverse(self, A):
    if(A.left is not None):
        self.traverse(A.left)
    if(self.prev is not None and self.prev > A.val):
        if(self.first is None):
            self.first = self.prev
            self.last = A.val
        else:
            self.last = A.val
    self.prev = A.val
    if(A.right is not None):
        self.traverse(A.right)