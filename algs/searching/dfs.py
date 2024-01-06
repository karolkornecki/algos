from shared.tree_node import TreeNode


def dfs(node: TreeNode, fn):
    # visited is not needed because lack of backward reference
    queue = [node]
    while queue:
        n = queue.pop()  # hint: compare with bfs just one line difference
        fn(n.key)
        if n.right is not None:
            queue.append(n.right)
        if n.left is not None:
            queue.append(n.left)
