import unittest

from graphs.digraph import Digraph
from graphs.topological_sort import topological_sort


class TopologicalSortTestCase(unittest.TestCase):

    def test_topological_sort(self):
        # given
        g = Digraph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(0, 5)
        g.add_edge(1, 4)
        g.add_edge(6, 0)
        g.add_edge(6, 4)
        g.add_edge(3, 6)
        g.add_edge(3, 4)
        g.add_edge(3, 2)
        g.add_edge(3, 5)
        g.add_edge(5, 2)

        # when
        result = topological_sort(g)

        # then
        self.assertEqual([3, 6, 0, 5, 2, 1, 4], result)


if __name__ == '__main__':
    unittest.main()
