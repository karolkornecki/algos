import unittest

from searching.bfs import bfs
from shared.util import array_to_tree


class BfsTestCase(unittest.TestCase):

    def test_bfs(self):
        # given
        root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
        # when
        result = []
        bfs(root, lambda v: result.append(v))
        # then
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], result)


if __name__ == '__main__':
    unittest.main()
