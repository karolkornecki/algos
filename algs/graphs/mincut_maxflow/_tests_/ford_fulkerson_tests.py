import unittest

from graphs.mincut_maxflow.flow_edge import FlowEdge
from graphs.mincut_maxflow.flow_network import FlowNetwork
from graphs.mincut_maxflow.ford_fulkerson import FordFulkerson


class FordFulkersonTestCase(unittest.TestCase):

    def test_ford_fulkerson_maxflow_1(self):
        # given
        network = FlowNetwork()
        network.add_edge(FlowEdge('s', 'A', 10.0))
        network.add_edge(FlowEdge('s', 'B', 5.0))
        network.add_edge(FlowEdge('s', 'C', 15.0))
        network.add_edge(FlowEdge('A', 'D', 9.0))
        network.add_edge(FlowEdge('A', 'E', 15.0))
        network.add_edge(FlowEdge('A', 'B', 4.0))
        network.add_edge(FlowEdge('B', 'E', 8.0))
        network.add_edge(FlowEdge('B', 'C', 4.0))
        network.add_edge(FlowEdge('C', 'F', 16.0))
        network.add_edge(FlowEdge('D', 't', 10.0))
        network.add_edge(FlowEdge('D', 'E', 15.0))
        network.add_edge(FlowEdge('E', 't', 10.0))
        network.add_edge(FlowEdge('E', 'F', 15.0))
        network.add_edge(FlowEdge('F', 'B', 6.0))
        network.add_edge(FlowEdge('F', 't', 10.0))
        # when
        ff = FordFulkerson(network, 's', 't')
        # then
        self.assertEqual(ff.value(), 28)

    def test_ford_fulkerson_maxflow_2(self):
        # given
        s = 5
        t = 4
        network = FlowNetwork()
        network.add_edge(FlowEdge(s, 0, 10))
        network.add_edge(FlowEdge(s, 1, 10))
        network.add_edge(FlowEdge(2, t, 10))
        network.add_edge(FlowEdge(3, t, 10))
        network.add_edge(FlowEdge(0, 1, 2))
        network.add_edge(FlowEdge(0, 2, 4))
        network.add_edge(FlowEdge(0, 3, 8))
        network.add_edge(FlowEdge(1, 3, 9))
        network.add_edge(FlowEdge(3, 2, 6))
        # when
        ff = FordFulkerson(network, s, t)
        # then
        self.assertEqual(ff.value(), 19)
