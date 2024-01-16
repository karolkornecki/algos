import unittest

from graphs.undirected_graph import Graph


class UndirectedGraphTestCase(unittest.TestCase):

    def test_undirected_graph(self):
        # given
        g = Graph()
        # when
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        # then
        self.assertEqual(4, g.V())
        self.assertEqual(3, g.E())


if __name__ == '__main__':
    unittest.main()
