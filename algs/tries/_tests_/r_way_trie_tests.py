import unittest

from tries.r_way_trie import Trie


class RWayTrieTestCase(unittest.TestCase):

    def test_r_wat_trie(self):
        # when
        trie = Trie()
        trie.insert("house")
        trie.insert("cat")
        trie.insert("dog")
        trie.insert("permission")
        trie.insert(None)
        trie.insert("")
        # then
        self.assertTrue(trie.search("house"))
        self.assertTrue(trie.search("cat"))
        self.assertTrue(trie.search("dog"))
        self.assertTrue(trie.search("permission"))
        self.assertFalse(trie.search("rabbit"))
        self.assertFalse(trie.search("home"))
        self.assertFalse(trie.search(None))
        self.assertFalse(trie.search(""))
