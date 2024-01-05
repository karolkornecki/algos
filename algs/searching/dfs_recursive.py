from shared.tree_node import TreeNode


def dfs(node: TreeNode, fn):
    # visited is not needed because lack of backward reference
    if node is None:
        return
    fn(node.v)
    dfs(node.left, fn)
    dfs(node.right, fn)
