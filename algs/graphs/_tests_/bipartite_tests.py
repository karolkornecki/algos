import unittest

from graphs.bipartite import Bipartite
from graphs.graph import Graph


class BipartiteTestCase(unittest.TestCase):

    def test_should_be_bipartite(self):
        # given
        g = Graph()
        g.add_edge(1, 10)
        g.add_edge(1, 40)
        g.add_edge(2, 30)
        g.add_edge(3, 10)
        g.add_edge(3, 20)
        g.add_edge(4, 30)
        g.add_edge(4, 40)
        g.add_edge(5, 40)
        # when
        b = Bipartite(g)
        # then
        self.assertTrue(b.is_bipartite)

    def test_should_not_be_bipartite(self):
        # given
        g = Graph()
        g.add_edge(1, 10)
        g.add_edge(1, 40)
        g.add_edge(2, 30)
        g.add_edge(3, 10)
        g.add_edge(3, 20)
        g.add_edge(4, 30)
        g.add_edge(4, 40)
        g.add_edge(5, 40)
        g.add_edge(5, 4)
        # when
        b = Bipartite(g)
        # then
        self.assertFalse(b.is_bipartite)


if __name__ == '__main__':
    unittest.main()
