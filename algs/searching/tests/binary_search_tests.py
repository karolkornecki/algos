import unittest

from parameterized import parameterized

from searching.binary_search import binary_search, binary_search_iter


class BinarySearchTestCase(unittest.TestCase):

    @parameterized.expand([(None, 1, None),
                           ([], 1, None),
                           ([1], 1, 0),
                           ([1], 2, None),
                           ([1, 2, 3, 4], 1, 0),
                           ([1, 2, 3, 4], 2, 1),
                           ([1, 2, 3, 4], 3, 2),
                           ([1, 2, 3, 4], 4, 3),
                           ([1, 2, 3, 4], 5, None),
                           ([1, 2, 3], 1, 0),
                           ([1, 2, 3], 2, 1),
                           ([1, 2, 3], 3, 2),
                           ([1, 2, 3], 4, None),
                           ])
    def test_binary_search(self, array, k, expected):
        # when
        result = binary_search(array, k)
        # then
        self.assertEqual(expected, result)

    @parameterized.expand([(None, 1, None),
                           ([], 1, None),
                           ([1], 1, 0),
                           ([1], 2, None),
                           ([1, 2, 3, 4], 1, 0),
                           ([1, 2, 3, 4], 2, 1),
                           ([1, 2, 3, 4], 3, 2),
                           ([1, 2, 3, 4], 4, 3),
                           ([1, 2, 3, 4], 5, None),
                           ([1, 2, 3], 1, 0),
                           ([1, 2, 3], 2, 1),
                           ([1, 2, 3], 3, 2),
                           ([1, 2, 3], 4, None),
                           ])
    def test_binary_search_iter(self, array, k, expected):
        # when
        result = binary_search_iter(array, k)
        # then
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
