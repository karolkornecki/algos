import unittest

from substring_search.knuth_morris_pratt import kmp


class KnuthMorrisPrattTestCase(unittest.TestCase):

    def test_kmp_1(self):
        # given
        pattern = "ababac"
        text = "aabacaababacaa"
        # when
        i = kmp(text, pattern)
        # then
        self.assertEqual(6, i)

    def test_kmp_2(self):
        # given
        pattern = "hasa"
        text = "alahasacat"
        # when
        i = kmp(text, pattern)
        # then
        self.assertEqual(3, i)

    def test_kmp__not_found(self):
        # given
        pattern = "not"
        text = "alahasacat"
        # when
        i = kmp(text, pattern)
        # then
        self.assertEqual(-1, i)
