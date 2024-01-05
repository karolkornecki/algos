import unittest

from searching.inorder_traversal import inorder_traversal
from shared.util import array_to_tree


class InOrderTraversalTestCase(unittest.TestCase):

    def test_inorder_traversal(self):
        # given
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # when
        result = []
        inorder_traversal(root, lambda v: result.append(v))
        # then
        self.assertEqual([4, 2, 5, 1, 6, 3, 7], result)


if __name__ == '__main__':
    unittest.main()
