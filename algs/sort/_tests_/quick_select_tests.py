import unittest

from parameterized import parameterized

from sort import quick_select as qs


class QuickSelectTestCase(unittest.TestCase):

    def test_quick_select(self):
        # given
        a1 = [7, 6, 5, 4, 3, 2, 1]
        a2 = [8, 6, 7, 4, 1, 2, 5, 3]
        # then
        r1 = qs.quick_select(a1, 5)
        r2 = qs.quick_select(a2, 3)
        # then
        self.assertEqual(6, r1)
        self.assertEqual(4, r2)

    @parameterized.expand([(None, 1), ([], 1), ([1], 2)])
    def test_should_quick_select_throw_exception(self, given_array, kth):
        # when
        with self.assertRaises(Exception) as context:
            qs.quick_select(given_array, kth)
        # then
        self.assertTrue('invalid arguments' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
