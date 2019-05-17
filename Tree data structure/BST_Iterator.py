# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

#  Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# Try to optimize the additional space complexity apart from the amortized time complexity. 
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

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        if root:
            self.items = [root]
            self.current = root.left
        else:
            self.items = None
            self.current = None

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.items:
            return True
        return False
        
    # @return an integer, the next smallest number
    def next(self):
        while self.current:
            self.items.append(self.current)
            self.current = self.current.left
        while self.items:
            temp = self.items.pop()
            res = temp.val
            if temp.right:
                cur = temp.right
                self.items.append(temp.right)
                while cur.left:
                    #print("Pushing",cur.left.val)
                    self.items.append(cur.left)
                    cur= cur.left
            return res

root = createTree()
i = BSTIterator(root)
while i.hasNext():
    print(i.next())



