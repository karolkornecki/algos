import unittest

from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph
from graphs.minimum_spanning_tree.lazy_prim_mst import LazyPrimMST


class LazyPrimMSTTestCase(unittest.TestCase):

    def test_should_find_mst(self):
        # given
        g = EdgeWeightedGraph()
        g.add_edge(Edge(0, 7, 0.16))
        g.add_edge(Edge(2, 3, 0.17))
        g.add_edge(Edge(1, 7, 0.19))
        g.add_edge(Edge(0, 2, 0.26))
        g.add_edge(Edge(5, 7, 0.28))
        g.add_edge(Edge(1, 3, 0.29))
        g.add_edge(Edge(1, 5, 0.32))
        g.add_edge(Edge(2, 7, 0.34))
        g.add_edge(Edge(4, 5, 0.35))
        g.add_edge(Edge(1, 2, 0.36))
        g.add_edge(Edge(4, 7, 0.37))
        g.add_edge(Edge(0, 4, 0.38))
        g.add_edge(Edge(6, 2, 0.40))
        g.add_edge(Edge(3, 6, 0.52))
        g.add_edge(Edge(6, 0, 0.58))
        g.add_edge(Edge(6, 4, 0.93))
        # when
        mst = LazyPrimMST(g)
        # then
        self.assertEqual(1.81, mst.weight)
        self.assertEqual(g.V() - 1, len(mst.edges()))  # mst always has V-1 edges
        mst_edges = mst.edges()
        self.assertTrue(Edge(0, 7, 0.16) in mst_edges)
        self.assertTrue(Edge(2, 3, 0.17) in mst_edges)
        self.assertTrue(Edge(1, 7, 0.19) in mst_edges)
        self.assertTrue(Edge(0, 2, 0.26) in mst_edges)
        self.assertTrue(Edge(5, 7, 0.28) in mst_edges)
        self.assertTrue(Edge(4, 5, 0.35) in mst_edges)
        self.assertTrue(Edge(6, 2, 0.40) in mst_edges)


if __name__ == '__main__':
    unittest.main()
