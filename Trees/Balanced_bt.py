# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def checkBalance(root):
           if not root:return [True,0]
           left,right = checkBalance(root.left),checkBalance(root.right)
           balance = left[0] and right[0] and(abs(left[1]-right[1])<=1)
           return [balance,max(left[1],right[1])+1]
        return checkBalance(root)[0]
        
