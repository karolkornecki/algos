from shared.tree_node import TreeNode
from shared.util import array_to_tree


def postorder_traversal(tree: TreeNode, fn):
    if tree is None:
        return
    postorder_traversal(tree.left, fn)
    postorder_traversal(tree.right, fn)
    fn(tree.v)


if __name__ == '__main__':
    root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
    postorder_traversal(root, print)
