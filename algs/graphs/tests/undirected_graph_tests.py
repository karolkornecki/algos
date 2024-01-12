import unittest

from graphs.undirected_graph import UndirectedGraph


class UndirectedGraphTestCase(unittest.TestCase):

    def test_undirected_graph(self):
        # given
        g = UndirectedGraph()
        # when
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        # then
        self.assertEqual(4, g.v())
        self.assertEqual(3, g.e())


if __name__ == '__main__':
    unittest.main()
