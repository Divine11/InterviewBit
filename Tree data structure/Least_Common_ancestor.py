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


def findLCAUtil(root, n1, n2, v): 
      
    # Base Case 
    if root is None: 
        return None
  
    # IF either n1 or n2 matches ith root's key, report 
    # the presence by setting v1 or v2 as true and return 
    # root (Note that if a key is ancestor of other, then  
    # the ancestor key becomes LCA) 
    if root.val == n1 : 
        v[0] = True
        return root 
  
    if root.val == n2: 
        v[1] = True
        return root 
  
    # Look for keys in left and right subtree 
    left_lca = findLCAUtil(root.left, n1, n2, v) 
    right_lca = findLCAUtil(root.right, n1, n2, v) 
  
    # If both of the above calls return Non-NULL, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca: 
        return root  
  
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca is not None else right_lca 

def find(root, k): 
      
    # Base Case 
    if root is None: 
        return False
      
    # If key is present at root, or if left subtree or right 
    # subtree , return true 
    if (root.val == k or find(root.left, k) or
        find(root.right, k)): 
        return True
      
    # Else return false 
    return False

def findLCA(root, n1, n2): 
      
    # Initialize n1 and n2 as not visited 
    v = [False, False] 
  
    # Find lac of n1 and n2 using the technique discussed above 
    lca = findLCAUtil(root, n1, n2, v) 
  
    # Returns LCA only if both n1 and n2 are present in tree 
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and 
        find(lca, n1)): 
        return lca.val 
  
    # Else return None 
    return -1

print(findLCA(createTree(),97,9))

        