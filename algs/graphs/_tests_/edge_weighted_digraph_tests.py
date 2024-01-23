import unittest

from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph


class EdgeWeightedDigraphTestCase(unittest.TestCase):

    def test_edge_weighted_digraph(self):
        # given
        g = EdgeWeightedDigraph()
        # when
        g.add_edge(DirectedEdge(1, 2, 0.1))
        g.add_edge(DirectedEdge(1, 3, 0.2))
        g.add_edge(DirectedEdge(2, 4, 0.5))
        g.add_edge(DirectedEdge(2, 4, 0.5))
        # then
        self.assertEqual(4, g.V())
        self.assertEqual(3, g.E())
        self.assertEqual(3, len(g.edges()))
        self.assertEqual(2, len(g.adj(1)))
        self.assertEqual(1, len(g.adj(2)))
        self.assertEqual(0, len(g.adj(3)))
        self.assertEqual(0, len(g.adj(4)))
        self.assertTrue(DirectedEdge(1, 2, 0.1) in g.edges())
        self.assertTrue(DirectedEdge(2, 4, 0.5) in g.edges())
        self.assertTrue(DirectedEdge(1, 3, 0.2) in g.edges())


if __name__ == '__main__':
    unittest.main()
