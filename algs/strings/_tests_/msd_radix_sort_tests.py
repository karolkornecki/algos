import unittest

from strings.msd_radix_sort import msd_sort


class MSDRadixSortTestCase(unittest.TestCase):

    def test_msd_radix_sort(self):
        # given
        a = [
            "she",
            "sells",
            "seashells",
            "by",
            "the",
            "sea",
            "shore",
            "the",
            "shells",
            "she",
            "sells",
            "are",
            "surely",
            "seashells",
        ]
        # when
        msd_sort(a)
        # then
        self.assertEqual([
            "are",
            "by",
            "sea",
            "seashells",
            "seashells",
            "sells",
            "sells",
            "she",
            "she",
            "shells",
            "shore",
            "surely",
            "the",
            "the",
        ], a)
