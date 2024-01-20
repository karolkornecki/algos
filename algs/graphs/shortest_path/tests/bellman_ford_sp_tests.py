import unittest

from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph
from graphs.shortest_path.bellman_ford_sp import BellmanFordSP


class DijkstraSPTestCase(unittest.TestCase):

    def test_should_find_all_sp_from_s_vertex(self):
        # given
        g = EdgeWeightedDigraph()
        g.add_edge(DirectedEdge(0, 1, 5.0))
        g.add_edge(DirectedEdge(0, 4, 9.0))
        g.add_edge(DirectedEdge(0, 7, 8.0))
        g.add_edge(DirectedEdge(1, 2, 12.0))
        g.add_edge(DirectedEdge(1, 3, 15.0))
        g.add_edge(DirectedEdge(1, 7, 4.0))
        g.add_edge(DirectedEdge(2, 3, 3.0))
        g.add_edge(DirectedEdge(2, 6, 11.0))
        g.add_edge(DirectedEdge(3, 6, 9.0))
        g.add_edge(DirectedEdge(4, 5, 4.0))
        g.add_edge(DirectedEdge(4, 6, 20.0))
        g.add_edge(DirectedEdge(4, 7, 5.0))
        g.add_edge(DirectedEdge(5, 2, 1.0))
        g.add_edge(DirectedEdge(5, 6, 13.0))
        g.add_edge(DirectedEdge(7, 5, 6.0))
        g.add_edge(DirectedEdge(7, 2, 7.0))
        # when
        bellman_ford = BellmanFordSP(g, 0)
        # then
        # shortest paths distances
        self.assertEqual(0, bellman_ford.distance_to(0))
        self.assertEqual(5, bellman_ford.distance_to(1))
        self.assertEqual(14, bellman_ford.distance_to(2))
        self.assertEqual(17, bellman_ford.distance_to(3))
        self.assertEqual(9, bellman_ford.distance_to(4))
        self.assertEqual(13, bellman_ford.distance_to(5))
        self.assertEqual(25, bellman_ford.distance_to(6))
        self.assertEqual(8, bellman_ford.distance_to(7))
        # shortest paths
        self.assertEqual([], bellman_ford.path_to(0))
        self.assertEqual([
            DirectedEdge(0, 1, 5.0)],
            bellman_ford.path_to(1))
        self.assertEqual([
            DirectedEdge(5, 2, 1.0),
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)],
            bellman_ford.path_to(2))
        self.assertEqual([
            DirectedEdge(2, 3, 3.0),
            DirectedEdge(5, 2, 1.0),
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)],
            bellman_ford.path_to(3))
        self.assertEqual([
            DirectedEdge(0, 4, 9.0)
        ], bellman_ford.path_to(4))
        self.assertEqual([
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)
        ], bellman_ford.path_to(5))
        self.assertEqual([
            DirectedEdge(2, 6, 11.0),
            DirectedEdge(5, 2, 1.0),
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)
        ], bellman_ford.path_to(6))
        self.assertEqual([
            DirectedEdge(0, 7, 8.0)
        ], bellman_ford.path_to(7))

    def test_should_find_negative_cycle(self):
        # given
        g = EdgeWeightedDigraph()
        g.add_edge(DirectedEdge(4, 5, 0.35))
        g.add_edge(DirectedEdge(5, 4, -0.66))
        g.add_edge(DirectedEdge(4, 7, 0.37))
        g.add_edge(DirectedEdge(5, 7, 0.28))
        g.add_edge(DirectedEdge(7, 5, 0.28))
        g.add_edge(DirectedEdge(5, 1, 0.32))
        g.add_edge(DirectedEdge(0, 4, 0.38))
        g.add_edge(DirectedEdge(0, 2, 0.26))
        g.add_edge(DirectedEdge(7, 3, 0.39))
        g.add_edge(DirectedEdge(1, 3, 0.29))
        g.add_edge(DirectedEdge(2, 7, 0.34))
        g.add_edge(DirectedEdge(6, 2, 0.40))
        g.add_edge(DirectedEdge(3, 6, 0.52))
        g.add_edge(DirectedEdge(6, 0, 0.58))
        g.add_edge(DirectedEdge(6, 4, 0.93))
        # when
        bellman_ford = BellmanFordSP(g, 0)
        # then
        self.assertTrue(len(bellman_ford.cycle) > 0)
        self.assertEqual([
            DirectedEdge(5, 4, -0.66),
            DirectedEdge(4, 5, 0.35)
        ], bellman_ford.cycle)


if __name__ == '__main__':
    unittest.main()
