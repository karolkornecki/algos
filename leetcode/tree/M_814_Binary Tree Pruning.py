# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# shorter, simplified solution
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root


# Runtime 34ms Beats 75.47% of users with Python3
# Memory 16.48MB Beats 93.53% of users with Python3
# Runtime 34ms Beats 75.47% of users with Python3
# Memory 16.48MB Beats 93.53% of users with Python3
class Solution2:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        is_zero = self.prune(root)
        if is_zero:
            return None
        return root

    def prune(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return True
        is_left_zero = self.prune(node.left)
        is_right_zero = self.prune(node.right)
        if is_left_zero:
            node.left = None
        if is_right_zero:
            node.right = None

        if is_left_zero and is_right_zero and node.val == 0:
            return True
        return False


if __name__ == '__main__':
    t = TreeNode(1)
    t1r = TreeNode(0)
    t.right = t1r
    t2l = TreeNode(0)
    t2r = TreeNode(1)
    t1r.left = t2l
    t1r.right = t2r

    s = Solution()
    t = s.pruneTree(t)
    print(t)
