import unittest

from graphs.edge import Edge


class EdgeTestCase(unittest.TestCase):

    def test_edge(self):
        # given
        e = Edge(1, 2, 0.6)
        # expect
        self.assertTrue(1, e.either())
        self.assertTrue(1, e.other())
        self.assertTrue(2, e.other(1))
        self.assertTrue(0.6, e.weight)


if __name__ == '__main__':
    unittest.main()
