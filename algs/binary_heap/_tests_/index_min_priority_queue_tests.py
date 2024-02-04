import unittest

from binary_heap.index_min_priority_queue import IndexMinPriorityQueue


class IndexMinPriorityQueueTestCase(unittest.TestCase):

    def test_priority_queue_order(self):
        # given
        a1 = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a1:
            pq.insert(i, e)
            i += 1

        result = []
        while not pq.is_empty():
            result.append(pq.min_key())
            pq.del_min()
        # then
        self.assertEqual([1, 2, 2, 3, 5, 6, 7, 8], result)

    def test_priority_queue_size(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a:
            pq.insert(i, e)
            i += 1
        # then
        self.assertEqual(len(a), pq.size())

    def test_priority_queue_min(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a:
            pq.insert(i, e)
            i += 1
        # then
        self.assertFalse(pq.is_empty())
        self.assertEqual(1, pq.min_key())
        self.assertEqual(5, pq.min_index())
        self.assertEqual(1, pq.key_of(5))
        self.assertEqual(8, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(2, pq.min_key())
        self.assertEqual(7, pq.min_index())
        self.assertEqual(2, pq.key_of(7))
        self.assertEqual(7, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(2, pq.min_key())
        self.assertEqual(1, pq.min_index())
        self.assertEqual(2, pq.key_of(1))
        self.assertEqual(6, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(3, pq.min_key())
        self.assertEqual(2, pq.min_index())
        self.assertEqual(3, pq.key_of(2))
        self.assertEqual(5, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(5, pq.min_key())
        self.assertEqual(6, pq.min_index())
        self.assertEqual(5, pq.key_of(6))
        self.assertEqual(4, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(6, pq.min_key())
        self.assertEqual(4, pq.min_index())
        self.assertEqual(6, pq.key_of(4))
        self.assertEqual(3, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(7, pq.min_key())
        self.assertEqual(0, pq.min_index())
        self.assertEqual(7, pq.key_of(0))
        self.assertEqual(2, pq.size())
        pq.del_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(8, pq.min_key())
        self.assertEqual(3, pq.min_index())
        self.assertEqual(8, pq.key_of(3))
        # # now size should be 1
        self.assertFalse(pq.is_empty())
        self.assertEqual(1, pq.size())
        pq.del_min()
        # now should be empty
        self.assertTrue(pq.is_empty())

    def test_priority_queue_decrease_key(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a:
            pq.insert(i, e)
            i += 1
        # then
        self.assertEqual(1, pq.min_key())
        min_index = pq.min_index()
        # when
        pq.decrease_key(min_index, -10)
        # then
        self.assertEqual(-10, pq.min_key())
        self.assertEqual(min_index, pq.min_index())

    def test_priority_queue_increase_key(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a:
            pq.insert(i, e)
            i += 1
        # then
        self.assertEqual(1, pq.min_key())
        min_index = pq.min_index()
        # when
        pq.increase_key(min_index, 10)
        # then
        self.assertEqual(2, pq.min_key())
        self.assertNotEqual(min_index, pq.min_index())
        self.assertEqual(2, pq.key_of(pq.min_index()))

    def test_priority_queue_contains_and_delete(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a:
            pq.insert(i, e)
            i += 1
        # then
        self.assertTrue(pq.contains(0))
        self.assertTrue(pq.contains(1))
        self.assertTrue(pq.contains(2))
        self.assertTrue(pq.contains(3))
        self.assertTrue(pq.contains(4))
        self.assertTrue(pq.contains(5))
        self.assertTrue(pq.contains(6))
        self.assertTrue(pq.contains(7))
        # and not contains
        self.assertFalse(pq.contains(8))
        self.assertFalse(pq.contains(9))
        self.assertFalse(pq.contains(10))
        # now deleting existing indexes
        pq.delete(0)
        self.assertFalse(pq.contains(0))
        pq.delete(1)
        self.assertFalse(pq.contains(1))
        pq.delete(2)
        self.assertFalse(pq.contains(2))
        pq.delete(3)
        self.assertFalse(pq.contains(3))
        pq.delete(4)
        self.assertFalse(pq.contains(4))
        pq.delete(5)
        self.assertFalse(pq.contains(5))
        pq.delete(6)
        self.assertFalse(pq.contains(6))
        pq.delete(7)
        self.assertFalse(pq.contains(7))
        self.assertTrue(pq.is_empty())

    def test_priority_queue_change_key(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = IndexMinPriorityQueue()
        i = 0
        for e in a:
            pq.insert(i, e)
            i += 1
        # then
        pq.change_key(0, 70)
        self.assertEqual(70, pq.key_of(0))
        pq.change_key(1, 20)
        self.assertEqual(20, pq.key_of(1))
        pq.change_key(2, 30)
        self.assertEqual(30, pq.key_of(2))

    def test_should_throw_exception_when_min_invoked_on_empty_queue(self):
        pq = IndexMinPriorityQueue()
        # when
        with self.assertRaises(Exception) as context:
            pq.min_key()
        # then
        self.assertTrue('pq is empty' in str(context.exception))

    def test_should_throw_exception_when_pop_min_invoked_on_empty_queue(self):
        pq = IndexMinPriorityQueue()
        # when
        with self.assertRaises(Exception) as context:
            pq.del_min()
        # then
        self.assertTrue('pq is empty' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
