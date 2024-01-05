from shared.tree_node import TreeNode


def array_to_tree(array):
    def a_to_tree(a, root):
        if root >= len(a):
            return None
        if a[root] is None:
            return None
        tree = TreeNode(a[root])
        tree.left = a_to_tree(a, 2 * root + 1)
        tree.right = a_to_tree(a, 2 * root + 2)
        return tree

    return a_to_tree(array, 0)
