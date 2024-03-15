import unittest

from graphs.directed_cycle import DirectedCycle
from graphs.digraph import Digraph


class DirectedCycleTestCase(unittest.TestCase):

    def test_should_have_cycle(self):
        # given
        g = Digraph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        # when
        cycle = DirectedCycle(g)
        # then
        self.assertTrue(cycle.has_cycle)

    def test_should_not_have_cycle(self):
        # given
        g = Digraph()
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        # when
        cycle = DirectedCycle(g)
        # then
        self.assertFalse(cycle.has_cycle)


if __name__ == '__main__':
    unittest.main()
