from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    # 44 ms
    # 17.5 MB
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [(1, root)]
        h = 0
        while queue:
            dist, node = queue.pop()
            h = max(h, dist)
            if node.left is not None:
                queue.append((dist + 1, node.left))
            if node.right is not None:
                queue.append((dist + 1, node.right))
        return h

    # recursive
    # 38 ms
    # 17.8 MB
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1
