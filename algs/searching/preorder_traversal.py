from shared.tree_node import TreeNode
from shared.util import array_to_tree


def preorder_traversal(tree: TreeNode, fn):
    if tree is None:
        return
    fn(tree.key)
    preorder_traversal(tree.left, fn)
    preorder_traversal(tree.right, fn)


if __name__ == '__main__':
    root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
    preorder_traversal(root, print)
