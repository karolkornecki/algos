import unittest

from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph
from graphs.shortest_path.dijkstra_sp import DijkstraSP


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
        dijkstra = DijkstraSP(g, 0)
        # then
        # shortest paths distances
        self.assertEqual(0, dijkstra.distance_to(0))
        self.assertEqual(5, dijkstra.distance_to(1))
        self.assertEqual(14, dijkstra.distance_to(2))
        self.assertEqual(17, dijkstra.distance_to(3))
        self.assertEqual(9, dijkstra.distance_to(4))
        self.assertEqual(13, dijkstra.distance_to(5))
        self.assertEqual(25, dijkstra.distance_to(6))
        self.assertEqual(8, dijkstra.distance_to(7))
        # shortest paths
        self.assertEqual([], dijkstra.path_to(0))
        self.assertEqual([
            DirectedEdge(0, 1, 5.0)],
            dijkstra.path_to(1))
        self.assertEqual([
            DirectedEdge(5, 2, 1.0),
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)],
            dijkstra.path_to(2))
        self.assertEqual([
            DirectedEdge(2, 3, 3.0),
            DirectedEdge(5, 2, 1.0),
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)],
            dijkstra.path_to(3))
        self.assertEqual([
            DirectedEdge(0, 4, 9.0)
        ], dijkstra.path_to(4))
        self.assertEqual([
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)
        ], dijkstra.path_to(5))
        self.assertEqual([
            DirectedEdge(2, 6, 11.0),
            DirectedEdge(5, 2, 1.0),
            DirectedEdge(4, 5, 4.0),
            DirectedEdge(0, 4, 9.0)
        ], dijkstra.path_to(6))
        self.assertEqual([
            DirectedEdge(0, 7, 8.0)
        ], dijkstra.path_to(7))


if __name__ == '__main__':
    unittest.main()
