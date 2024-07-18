# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right= dfs(root.right)
            res = max(res,left+right) #For each node check for max diameter
            return 1+max(left,right)  # Return max number of edges(l or r)
        dfs(root)
        return res
