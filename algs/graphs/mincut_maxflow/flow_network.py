from graphs.mincut_maxflow.flow_edge import FlowEdge


class FlowNetwork:
    """ Graph data type for calculating min-cut / max-flow"""

    def __init__(self):
        # vertex -> [edges]
        self.edges_dict = dict()

        self.all_edges = set()

    def V(self):
        """ Number of vertices"""
        return self.edges_dict.keys()

    def E(self):
        """Number of edges"""
        return len(self.all_edges)

    def adj(self, v) -> [FlowEdge]:
        return self.edges_dict[v]

    def add_edge(self, e: FlowEdge):
        v = e.src
        w = e.dest
        if v not in self.edges_dict:
            self.edges_dict[v] = set()
        if w not in self.edges_dict:
            self.edges_dict[w] = set()
        self.edges_dict[v].add(e)
        self.edges_dict[w].add(e)

    def edges(self) -> [FlowEdge]:
        return self.all_edges
