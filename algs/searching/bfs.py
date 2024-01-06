from shared.tree_node import TreeNode


def bfs(node: TreeNode, fn):
    queue = [node]
    # visited is not needed because lack of backward reference
    while queue:
        n = queue.pop(0)
        fn(n.key)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
