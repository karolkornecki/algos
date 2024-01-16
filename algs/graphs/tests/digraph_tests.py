import unittest

from graphs.digraph import Digraph


class DigraphTestCase(unittest.TestCase):

    def test_directed_graph(self):
        # given
        g = Digraph()
        # when
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        # then
        self.assertEqual(4, g.V())
        self.assertEqual(3, g.E())


if __name__ == '__main__':
    unittest.main()
