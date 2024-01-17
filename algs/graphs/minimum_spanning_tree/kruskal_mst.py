from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph
from union_find.weighted_quick_union_path_compression_uf import WeightedQuickUnionPathCompressionUF


# complexity E*logE
class KruskalMST:
    def __init__(self, g: EdgeWeightedGraph):
        self.g = g
        self.mst = []
        self.weight = 0
        # sort edges ascending
        edges = []
        for e in g.edges():
            edges.append(e)
        edges.sort()

        # !assumption: vertex in graph are ordered integers without gaps starting from 0!
        uf = WeightedQuickUnionPathCompressionUF(g.V())
        while edges and len(self.mst) < g.V() - 1:
            edge = edges.pop(0)
            v = edge.either()
            w = edge.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self.mst.append(edge)
                self.weight += edge.weight

    def edges(self) -> [Edge]:
        return self.mst
