from shared.tree_node import TreeNode
from shared.util import array_to_tree


def inorder_traversal(tree: TreeNode, fn):
    if tree is None:
        return
    inorder_traversal(tree.left, fn)
    fn(tree.v)
    inorder_traversal(tree.right, fn)


if __name__ == '__main__':
    root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
    inorder_traversal(root, print)
