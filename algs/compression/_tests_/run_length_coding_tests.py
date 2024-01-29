import unittest

from compression.run_length_coding import compress, uncompress


class RLCTestCase(unittest.TestCase):

    def test_rlc(self):
        # expect
        self.assertEqual(None, compress(None))
        self.assertEqual("", compress(""))
        self.assertEqual("4A", compress("AAAA"))
        self.assertEqual("1A", compress("A"))
        self.assertEqual("1A1B1C", compress("ABC"))
        self.assertEqual("3A3B", compress("AAABBB"))
        self.assertEqual("3A3B1C", compress("AAABBBC"))

        self.assertEqual(None, uncompress(None))
        self.assertEqual("", uncompress(""))
        self.assertEqual("DDDD", uncompress("4D"))
        self.assertEqual("DDDDABBBCAAAAAAAAAA", uncompress("4D1A3B1C10A"))
