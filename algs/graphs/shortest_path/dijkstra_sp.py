from binary_heap.index_min_priority_queue import IndexMinPriorityQueue
from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph

INFINITY = 2000000000


# single-source the shortest path. From vertex s to every other vertex
# works for graph with non-negative edges
# complexity E * logV
class DijkstraSP:
    def __init__(self, g: EdgeWeightedDigraph, s):
        # shortest distance to given vertex from s
        self.dist_to = dict()
        # edges on shortest path
        self.edge_to = dict()
        # starting vertex
        self.s = s

        # initialize with infinity
        for v in g.vertices():
            self.dist_to[v] = INFINITY

        # from 0 to itself distance is 0
        self.dist_to[s] = 0

        pq = IndexMinPriorityQueue()
        pq.insert(s, self.dist_to[s])
        while not pq.is_empty():
            v = pq.del_min()
            for edge in g.adj(v):
                w = edge.dest()
                if self.dist_to[w] > self.dist_to[v] + edge.weight:
                    self.dist_to[w] = self.dist_to[v] + edge.weight
                    self.edge_to[w] = edge
                    if pq.contains(w):
                        pq.decrease_key(w, self.dist_to[w])
                    else:
                        pq.insert(w, self.dist_to[w])

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
