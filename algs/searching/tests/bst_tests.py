import unittest

from searching.bst import BST


class BstTestCase(unittest.TestCase):

    def test_bst_is_empty(self):
        # given
        bst = BST()
        # then
        self.assertTrue(bst.is_empty())
        self.assertEqual(0, bst.size())
        # when
        bst.put('1', '')
        self.assertFalse(bst.is_empty())
        self.assertEqual(1, bst.size())
        # and when
        bst.put('2', '')
        # then
        self.assertFalse(bst.is_empty())
        self.assertEqual(2, bst.size())

    def test_bst_put(self):
        # given
        bst = BST()
        # when
        bst.put('4', '4')
        bst.put('6', '6')
        bst.put('1', '1')
        bst.put('8', '8')
        bst.put('5', '5')
        bst.put('2', '2')
        # duplicate override
        bst.put('2', '7')
        # then
        self.assertTrue(bst.is_bst())
        self.assertEqual(6, bst.size())
        self.assertEqual('7', bst.get('2'))

    def test_bst_min(self):
        # given
        bst = BST()
        # when
        bst.put('4', '4')
        bst.put('6', '6')
        bst.put('1', '1')
        bst.put('8', '8')
        bst.put('5', '5')
        bst.put('2', '2')
        # then
        self.assertEqual('1', bst.min())
        # when deleted
        bst.del_min()
        # then 2 is next min
        self.assertEqual('2', bst.min())
        self.assertTrue(bst.is_bst())

    def test_bst_contains(self):
        # given
        bst = BST()
        # when
        bst.put('4', '4')
        bst.put('6', '6')
        bst.put('1', '1')
        bst.put('8', '8')
        bst.put('5', '5')
        bst.put('2', '2')
        # then
        self.assertTrue(bst.contains('4'))
        self.assertEqual(6, bst.size())
        # when deleted
        bst.delete('4')
        # then
        self.assertFalse(bst.contains('4'))
        self.assertEqual(5, bst.size())

    def test_bst_get(self):
        # given
        bst = BST()
        # when
        bst.put('4', '4')
        bst.put('6', '6')
        bst.put('1', '1')
        bst.put('8', '8')
        bst.put('5', '5')
        bst.put('2', '2')
        # then
        self.assertEqual('4', bst.get('4'))
        # when deleted
        bst.delete('4')
        # then
        self.assertEqual(None, bst.get('4'))

    def test_bst_height(self):
        # given
        bst = BST()
        # when
        bst.put('4', '4')
        # then
        self.assertEqual(1, bst.height())
        # and when
        bst.put('3', '3')
        self.assertEqual(2, bst.height())
        bst.put('5', '5')
        self.assertEqual(2, bst.height())
        bst.put('2', '2')
        self.assertEqual(3, bst.height())
        bst.put('1', '1')
        self.assertEqual(4, bst.height())

    def test_bst_rank(self):
        # given
        bst = BST()
        # when
        bst.put(4, '4')
        bst.put(6, '6')
        bst.put(1, '1')
        bst.put(8, '8')
        bst.put(5, '5')
        bst.put(2, '2')
        # then
        self.assertEqual(0, bst.rank(-100))
        self.assertEqual(0, bst.rank(1))
        self.assertEqual(1, bst.rank(2))
        self.assertEqual(2, bst.rank(3))  # non-existing key
        self.assertEqual(2, bst.rank(4))
        self.assertEqual(3, bst.rank(5))
        self.assertEqual(4, bst.rank(6))
        self.assertEqual(5, bst.rank(7))  # non-existing key
        self.assertEqual(5, bst.rank(8))
        self.assertEqual(6, bst.rank(9))
        self.assertEqual(6, bst.rank(100))


if __name__ == '__main__':
    unittest.main()
