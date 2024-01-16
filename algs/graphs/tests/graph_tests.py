import unittest

from graphs.graph import Graph


class GraphTestCase(unittest.TestCase):

    def test_graph(self):
        # given
        g = Graph()
        # when
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 4)
        # then
        self.assertEqual(4, g.V())
        self.assertEqual(3, g.E())


if __name__ == '__main__':
    unittest.main()
