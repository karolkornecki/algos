import unittest

from shared.interval import Interval


class IntervalTestCase(unittest.TestCase):

    def test_interval(self):
        # given
        interval = Interval(2, 9)
        # expect
        self.assertEqual(2, interval.min)
        self.assertEqual(9, interval.max)
        self.assertEqual(7, interval.length())

    def test_interval_intersection(self):
        # given
        interval = Interval(2, 9)
        # expect
        self.assertTrue(interval.intersect(Interval(8, 10)))
        self.assertFalse(interval.intersect(Interval(9, 10)))
        self.assertFalse(interval.intersect(Interval(11, 15)))

    def test_interval_has(self):
        # given
        interval = Interval(2, 9)
        # expect
        self.assertTrue(interval.has(2))
        self.assertTrue(interval.has(5))
        self.assertTrue(interval.has(9))
        self.assertFalse(interval.has(1))
        self.assertFalse(interval.has(10))

    def test_interval_contains_interval(self):
        # given
        interval = Interval(2, 9)
        # then
        self.assertTrue(interval.contains(Interval(2, 9)))
        self.assertTrue(interval.contains(Interval(2, 8)))
        self.assertTrue(interval.contains(Interval(3, 9)))
        self.assertTrue(interval.contains(Interval(3, 8)))
        self.assertFalse(interval.contains(Interval(1, 3)))
        self.assertFalse(interval.contains(Interval(9, 11)))
        self.assertFalse(interval.contains(Interval(10, 14)))

    def test_interval_merge(self):
        # given
        interval = Interval(2, 9)
        other = Interval(7, 13)
        # when
        merged = interval.merge(other)
        # then
        self.assertEqual(2, merged.min)
        self.assertEqual(13, merged.max)


if __name__ == '__main__':
    unittest.main()
