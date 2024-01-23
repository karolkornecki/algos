import unittest

from graphs.directed_edge import DirectedEdge


class DirectedEdgeTestCase(unittest.TestCase):

    def test_directed_edge(self):
        # given
        e = DirectedEdge(1, 2, 0.6)
        # expect
        self.assertTrue(1, e.src())
        self.assertTrue(2, e.dest())
        self.assertTrue(0.6, e.weight)


if __name__ == '__main__':
    unittest.main()
