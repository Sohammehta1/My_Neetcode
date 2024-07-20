# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        right_view = []
        queue = []
        if root:
            queue.append(root)
        while queue:
            val = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            right_view.append(val)
        return right_view