from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root,lb,rb):
            '''lb -> left boundary, rb->right boundary'''
            if not root:
                return True
            if root.val <=lb or root.val >=rb:
                return False
            return isValid(root.left,lb,min(rb,root.val)) and isValid(root.right,max(lb,root.val),rb)
        return isValid(root,-float('inf'),float('inf'))
        
