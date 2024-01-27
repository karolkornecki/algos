import unittest

from substring_search.boyer_moore import boyer_moore


class BoyerMooreTestCase(unittest.TestCase):

    def test_boyer_moore_1(self):
        # given
        pattern = "ababac"
        text = "aabacaababacaa"
        # when
        i = boyer_moore(text, pattern)
        # then
        self.assertEqual(6, i)

    def test_boyer_moore_2(self):
        # given
        pattern = "hasa"
        text = "alahasacat"
        # when
        i = boyer_moore(text, pattern)
        # then
        self.assertEqual(3, i)

    def test_boyer_moore_3(self):
        # given
        pattern = "new"
        text = "hello new world"
        # when
        i = boyer_moore(text, pattern)
        # then
        self.assertEqual(6, i)

    def test_boyer_moore__not_found(self):
        # given
        pattern = "not"
        text = "alahasacat"
        # when
        i = boyer_moore(text, pattern)
        # then
        self.assertEqual(-1, i)
