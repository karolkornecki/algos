import sys
from functools import reduce

from binary_heap.index_min_priority_queue import IndexMinPriorityQueue
from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph


# eager Prim algorithm
class PrimMST:
    def __init__(self, g: EdgeWeightedGraph):
        self.edge_to = [None for _ in range(g.V())]
        self.dist_to = [sys.maxsize for _ in range(g.V())]
        self.visited = set()
        self.pq = IndexMinPriorityQueue()
        # run Prim algorithm from each vertex
        for v in g.vertices():
            if v not in self.visited:
                self.prim(g, v)

    def prim(self, g: EdgeWeightedGraph, s):
        self.dist_to[s] = 0
        self.pq.insert(s, self.dist_to[s])
        while not self.pq.is_empty():
            v = self.pq.del_min()
            self.scan(g, v)

    def scan(self, g: EdgeWeightedGraph, v):
        self.visited.add(v)
        for e in g.adj(v):
            w = e.other(v)
            if w in self.visited:
                continue
            if e.weight < self.dist_to[w]:
                self.dist_to[w] = e.weight
                self.edge_to[w] = e
                if self.pq.contains(w):
                    self.pq.decrease_key(w, self.dist_to[w])
                else:
                    self.pq.insert(w, self.dist_to[w])

    def edges(self) -> [Edge]:
        mst = []
        for v in range(len(self.edge_to)):
            e = self.edge_to[v]
            if e is not None:
                mst.append(e)
        return mst

    def weight(self):
        return reduce(lambda acc, e: acc + e.weight, self.edges(), 0)
