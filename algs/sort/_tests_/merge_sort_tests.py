import unittest

from parameterized import parameterized

from sort import merge_sort as ms


class MergeSortTestCase(unittest.TestCase):

    def test_merge_sort_recursive(self):
        # given
        a1 = [7, 6, 5, 4, 3, 2, 1]
        a2 = [8, 6, 7, 4, 1, 2, 5, 3]
        # then
        ms.merge_sort(a1)
        ms.merge_sort(a2)
        # then
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], a1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], a2)

    def test_merge_sort_bottom_up(self):
        # given
        a1 = [7, 6, 5, 4, 3, 2, 1]
        a2 = [8, 6, 7, 4, 1, 2, 5, 3]
        # then
        ms.merge_sort_bu(a1)
        ms.merge_sort_bu(a2)
        # then
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], a1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], a2)

    @parameterized.expand([(None, None), ([], []), ([1], [1])])
    def test_should_merge_sort_do_nothing(self, array_to_sort, expected_result):
        # when
        ms.merge_sort(array_to_sort)
        # then
        self.assertEqual(expected_result, array_to_sort)

    @parameterized.expand([(None, None), ([], []), ([1], [1])])
    def test_should_merge_sort_bu_do_nothing(self, array_to_sort, expected_result):
        # when
        ms.merge_sort_bu(array_to_sort)
        # then
        self.assertEqual(expected_result, array_to_sort)


if __name__ == '__main__':
    unittest.main()
