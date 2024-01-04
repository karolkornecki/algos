import unittest

from parameterized import parameterized

from binary_heap import heap_sort as hs


class HeapSortTestCase(unittest.TestCase):

    def test_heap_sort(self):
        # given
        a1 = [7, 6, 5, 4, 3, 2, 1]
        a2 = [8, 6, 7, 4, 1, 2, 5, 3]
        # then
        hs.heap_sort(a1)
        hs.heap_sort(a2)
        # then
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], a1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], a2)

    @parameterized.expand([(None, None), ([], []), ([1], [1])])
    def test_should_heap_sort_return_original_array(self, array_to_sort, expected_result):
        # when
        hs.heap_sort(array_to_sort)
        # then
        self.assertEqual(expected_result, array_to_sort)


if __name__ == '__main__':
    unittest.main()
