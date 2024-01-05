import unittest

from searching.preorder_traversal import preorder_traversal
from shared.util import array_to_tree


class PreOrderTraversalTestCase(unittest.TestCase):

    def test_preorder_traversal(self):
        # given
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # when
        result = []
        preorder_traversal(root, lambda v: result.append(v))
        # then
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], result)


if __name__ == '__main__':
    unittest.main()
