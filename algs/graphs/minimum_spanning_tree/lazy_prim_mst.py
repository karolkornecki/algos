from binary_heap.min_priority_queue import MinPriorityQueue
from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph


# lazy Prim algorithm E*logE
class LazyPrimMST:
    def __init__(self, g: EdgeWeightedGraph):
        self.mst = []
        self.weight = 0
        self.visited = set()
        self.pq = MinPriorityQueue()
        # run Prim algorithm from each vertex
        for v in g.vertices():
            if v not in self.visited:
                self.prim(g, v)

    def prim(self, g: EdgeWeightedGraph, vertex):
        self.scan(g, vertex)
        while not self.pq.is_empty():
            edge = self.pq.pop_min()  # smallest edge
            v = edge.either()
            w = edge.other(v)
            assert v in self.visited or w in self.visited
            if v in self.visited and w in self.visited:
                continue
            self.mst.append(edge)
            self.weight += edge.weight
            if v not in self.visited:
                self.scan(g, v)
            if w not in self.visited:
                self.scan(g, w)

    def scan(self, g: EdgeWeightedGraph, v):
        self.visited.add(v)
        for e in g.adj(v):
            if e.other(v) not in self.visited:
                self.pq.insert(e)

    def edges(self) -> [Edge]:
        return self.mst
