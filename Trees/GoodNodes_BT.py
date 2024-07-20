from typing import Optional
# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodes(root,max_before)->int:
            if not root:
                return 0
            count = 0
            if root.val >=max_before:
                max_before = root.val
                count +=1
            left = countGoodNodes(root.left,max_before)
            right = countGoodNodes(root.right,max_before)
            return left+right+count
        return countGoodNodes(root,-101)
            
