import unittest

from graphs.digraph import Digraph
from graphs.strongly_connected_components import scc


class StronglyConnectedComponentsTestCase(unittest.TestCase):

    def test_strongly_connected_components(self):
        # given
        g = Digraph()
        g.add_edge(0, 1)
        g.add_edge(0, 5)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 2)
        g.add_edge(3, 5)
        g.add_edge(4, 2)
        g.add_edge(4, 3)
        g.add_edge(5, 4)
        g.add_edge(6, 8)
        g.add_edge(6, 9)
        g.add_edge(6, 4)
        g.add_edge(6, 0)
        g.add_edge(7, 6)
        g.add_edge(7, 9)
        g.add_edge(8, 6)
        g.add_edge(9, 10)
        g.add_edge(9, 11)
        g.add_edge(10, 12)
        g.add_edge(11, 12)
        g.add_edge(11, 4)
        g.add_edge(12, 9)

        # when
        number_of_cc, identifiers = scc(g)

        # then
        self.assertEqual(5, number_of_cc)
        self.assertEqual({
            0: 1,
            1: 0,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 3,
            7: 4,
            8: 3,
            9: 2,
            10: 2,
            11: 2,
            12: 2
        }, identifiers)


if __name__ == '__main__':
    unittest.main()
