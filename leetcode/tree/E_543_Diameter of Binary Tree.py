from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.diameter = max(self.diameter, l + r)
            return max(l, r) + 1

        depth(root)
        return self.diameter


if __name__ == '__main__':
    t = TreeNode(1)
    t3 = TreeNode(3)
    t2 = TreeNode(2)
    t.left = t2
    t.right = t3
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t2.left = t4
    t2.right = t5

    s = Solution()
    print(s.diameterOfBinaryTree(t))
