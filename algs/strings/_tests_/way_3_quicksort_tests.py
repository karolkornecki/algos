import unittest

from strings.way_3_quicksort import way_3_string_qs


class Way3QuickSortTestCase(unittest.TestCase):

    def test_way_3_quicksort(self):
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
        way_3_string_qs(a)
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
