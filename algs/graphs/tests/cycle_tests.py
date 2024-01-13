import unittest

from graphs.cycle import Cycle
from graphs.undirected_graph import UndirectedGraph


class CycleTestCase(unittest.TestCase):

    def test_should_have_cycle(self):
        # given
        g = UndirectedGraph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 5)
        g.add_edge(5, 6)
        g.add_edge(3, 6)
        # when
        cycle = Cycle(g)
        # then
        self.assertTrue(cycle.has_cycle)

    def test_should_not_have_cycle(self):
        # given
        g = UndirectedGraph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 5)
        g.add_edge(5, 6)
        # when
        cycle = Cycle(g)
        # then
        self.assertFalse(cycle.has_cycle)


if __name__ == '__main__':
    unittest.main()
