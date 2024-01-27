import unittest

from substring_search.rabin_karp import rabin_karp


class RabinKarpTestCase(unittest.TestCase):

    def test_rabin_karp_1(self):
        # given
        pattern = "ababac"
        text = "aabacaababacaa"
        # when
        i = rabin_karp(text, pattern)
        # then
        self.assertEqual(6, i)

    def test_rabin_karp_2(self):
        # given
        pattern = "hasa"
        text = "alahasacat"
        # when
        i = rabin_karp(text, pattern)
        # then
        self.assertEqual(3, i)

    def test_rabin_karp_3(self):
        # given
        pattern = "new"
        text = "hello new world"
        # when
        i = rabin_karp(text, pattern)
        # then
        self.assertEqual(6, i)

    def test_rabin_karp_same_length(self):
        # given
        pattern = "hello"
        text = "hello"
        # when
        i = rabin_karp(text, pattern)
        # then
        self.assertEqual(0, i)

    def test_rabin_karp__not_found(self):
        # given
        pattern = "not"
        text = "alahasacat"
        # when
        i = rabin_karp(text, pattern)
        # then
        self.assertEqual(-1, i)
