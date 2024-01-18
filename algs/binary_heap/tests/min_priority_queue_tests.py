import unittest

from binary_heap.min_priority_queue import MinPriorityQueue


class MinPriorityQueueTestCase(unittest.TestCase):

    def test_priority_queue_order(self):
        # given
        a1 = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = MinPriorityQueue()
        for e in a1:
            pq.insert(e)

        result = []
        while not pq.is_empty():
            result.append(pq.pop_min())
        # then
        self.assertEqual([1, 2, 2, 3, 5, 6, 7, 8], result)

    def test_priority_queue_size(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = MinPriorityQueue()
        for e in a:
            pq.insert(e)
        # then
        self.assertEqual(len(a), pq.size())

    def test_priority_queue_min(self):
        # given
        a = [7, 2, 3, 8, 6, 1, 5, 2]
        # when
        pq = MinPriorityQueue()
        for e in a:
            pq.insert(e)
        # then
        self.assertFalse(pq.is_empty())
        self.assertEqual(1, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(2, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(2, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(3, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(5, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(6, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(7, pq.min())
        pq.pop_min()
        self.assertFalse(pq.is_empty())
        self.assertEqual(8, pq.min())
        # now size should be 1
        self.assertFalse(pq.is_empty())
        self.assertEqual(1, pq.size())
        pq.pop_min()
        # now should be empty
        self.assertTrue(pq.is_empty())

    def test_should_throw_exception_when_min_invoked_on_empty_queue(self):
        pq = MinPriorityQueue()
        # when
        with self.assertRaises(Exception) as context:
            pq.min()
        # then
        self.assertTrue('queue is empty' in str(context.exception))

    def test_should_throw_exception_when_pop_min_invoked_on_empty_queue(self):
        pq = MinPriorityQueue()
        # when
        with self.assertRaises(Exception) as context:
            pq.pop_min()
        # then
        self.assertTrue('queue is empty' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
