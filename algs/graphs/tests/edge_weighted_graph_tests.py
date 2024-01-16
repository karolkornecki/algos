import unittest

from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph


class EdgeWeightedGraphTestCase(unittest.TestCase):

    def test_edge_weighted_graph(self):
        # given
        g = EdgeWeightedGraph()
        # when
        g.add_edge(Edge(1, 2, 0.1))
        g.add_edge(Edge(1, 3, 0.2))
        g.add_edge(Edge(2, 4, 0.5))
        g.add_edge(Edge(2, 4, 0.5))
        # then
        self.assertEqual(4, g.V())
        self.assertEqual(3, g.E())


if __name__ == '__main__':
    unittest.main()
