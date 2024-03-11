from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False
        queue = [(root, 0)]  # node,level
        values = []
        while queue:
            node, level = queue.pop(0)
            if level % 2 == node.val % 2:
                return False
            if len(values) <= level:
                values.append([node.val])
            else:
                if level % 2 == 0 and node.val <= values[level][len(values[level]) - 1]:
                    return False
                if level % 2 == 1 and node.val >= values[level][len(values[level]) - 1]:
                    return False
                values[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return True
