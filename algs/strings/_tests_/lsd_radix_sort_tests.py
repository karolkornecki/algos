import unittest

from strings.lsd_radix_sort import lsd_sort


class LSDRadixSortTestCase(unittest.TestCase):

    def test_lsd_radix_sort(self):
        # given
        a = [
            "dab",
            "add",
            "cab",
            "fad",
            "fee",
            "bad",
            "dad",
            "bee",
            "fed",
            "bed",
            "ebb",
            "ace",
        ]
        # when
        lsd_sort(a, 3)
        # then
        self.assertEqual([
            "ace",
            "add",
            "bad",
            "bed",
            "bee",
            "cab",
            "dab",
            "dad",
            "ebb",
            "fad",
            "fed",
            "fee",
        ], a)
