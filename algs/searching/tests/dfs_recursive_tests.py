import unittest

from searching.dfs_recursive import dfs
from shared.util import array_to_tree


class DfsRecursiveTestCase(unittest.TestCase):

    def test_dfs_recursive(self):
        # given
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # when
        result = []
        dfs(root, lambda v: result.append(v))
        # then
        self.assertEqual([1, 2, 4, 5, 3, 6, 7], result)


if __name__ == '__main__':
    unittest.main()
