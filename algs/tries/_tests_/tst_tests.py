import unittest

from tries.tst import TST


class TSTTestCase(unittest.TestCase):

    def test_tst(self):
        # when
        trie = TST()
        trie.put("house", 1)
        trie.put("cat", 2)
        trie.put("dog", 3)
        trie.put("permission", 4)
        trie.put(None, 5)
        trie.put("", 6)
        # then
        self.assertEqual(1, trie.get("house"))
        self.assertEqual(2, trie.get("cat"))
        self.assertEqual(3, trie.get("dog"))
        self.assertEqual(4, trie.get("permission"))
        self.assertFalse(trie.contains("rabbit"))
        self.assertFalse(trie.contains("home"))
        self.assertFalse(trie.contains(None))
        self.assertFalse(trie.contains(""))
        self.assertTrue(["house", "cat", "dog", "permission"], trie.keys())
        self.assertTrue(4, trie.size())
        # when
        trie.delete("house")
        # then
        self.assertEqual(3, trie.size())
        self.assertFalse(trie.contains("house"))
        self.assertTrue(["cat", "dog", "permission"], trie.keys())
        # when
        trie.delete("cat")
        # then
        self.assertEqual(2, trie.size())
        self.assertFalse(trie.contains("cat"))
        self.assertTrue(["dog", "permission"], trie.keys())
        # when
        trie.delete("dog")
        # then
        self.assertEqual(1, trie.size())
        self.assertFalse(trie.contains("dog"))
        self.assertTrue(["permission"], trie.keys())
        # when
        trie.delete("permission")
        # then
        self.assertEqual(0, trie.size())
        self.assertFalse(trie.contains("permission"))
        self.assertEqual(0, len(trie.keys()))
