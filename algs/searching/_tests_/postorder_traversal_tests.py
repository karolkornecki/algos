import unittest

from searching.postorder_traversal import postorder_traversal
from shared.util import array_to_tree


class PostOrderTraversalTestCase(unittest.TestCase):

    def test_postorder_traversal(self):
        # given
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # when
        result = []
        postorder_traversal(root, lambda v: result.append(v))
        # then
        self.assertEqual([4, 5, 2, 6, 7, 3, 1], result)


if __name__ == '__main__':
    unittest.main()
