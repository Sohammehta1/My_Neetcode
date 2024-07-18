from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: return False
        # Dividing the problem into 2 parts
        # 1 Checking if the subRoot exists in the tree
        # 2 If yes then checking for equality
        
       

        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))
        
        def findRoot(root,subRoot):
            if not root:
                return False
            if root.val == subRoot.val and isSameTree(root,subRoot):
                return True
            return findRoot(root.left,subRoot) or findRoot(root.right,subRoot)

            
        return findRoot(root,subRoot)
        

