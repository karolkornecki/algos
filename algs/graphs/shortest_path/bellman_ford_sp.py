from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph
from graphs.edge_weighted_directed_cycle import EdgeWeightedDirectedCycle

INFINITY = 2000000000
EPSILON = 1E-14


# single-source the shortest path. From vertex s to every other vertex
# works for graph with negative edges (but cannot have negative cycles)
# complexity E * V (slower than Dijkstra but handles negative edges)
class BellmanFordSP:
    def __init__(self, g: EdgeWeightedDigraph, s):
        # shortest distance to given vertex from s
        self.dist_to = dict()
        # edges on shortest path
        self.edge_to = dict()
        self.on_queue = set()
        # starting vertex
        self.s = s
        # number of calls to relax
        self.cost = 0
        self.cycle = []

        # initialize with infinity
        for v in g.vertices():
            self.dist_to[v] = INFINITY

        # from 0 to itself distance is 0
        self.dist_to[s] = 0

        self.queue = [s]
        self.on_queue.add(s)
        while self.queue and not self._has_negative_cycle():
            v = self.queue.pop(0)
            self.on_queue.remove(v)
            # relaxation
            for edge in g.adj(v):
                w = edge.dest()
                if self.dist_to[w] > self.dist_to[v] + edge.weight + EPSILON:
                    self.dist_to[w] = self.dist_to[v] + edge.weight
                    self.edge_to[w] = edge
                    if w not in self.on_queue:
                        self.queue.append(w)
                        self.on_queue.add(w)
                self.cost += 1
                if self.cost % g.V() == 0:
                    self._find_negative_cycle()
                    if self._has_negative_cycle():  # break if negative cycle found
                        return

    def distance_to(self, v) -> float:
        return self.dist_to[v]

    def path_to(self, v) -> [DirectedEdge]:
        if self.s == v:
            return []
        path = []
        edge = self.edge_to[v]
        while edge is not None:
            path.append(edge)
            if edge.src() in self.edge_to:
                edge = self.edge_to[edge.src()]
            else:
                edge = None
        return path

    def _has_negative_cycle(self):
        return len(self.cycle) > 0

    def _find_negative_cycle(self):
        graph = EdgeWeightedDigraph()
        for v in self.edge_to.keys():
            graph.add_edge(self.edge_to[v])
        cycle_finder = EdgeWeightedDirectedCycle(graph)
        self.cycle = cycle_finder.cycle
