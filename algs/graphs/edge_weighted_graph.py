from graphs.edge import Edge


class EdgeWeightedGraph:
    """
    Edge Weighted Undirected Graph
    """

    def __init__(self):
        self.edges = dict()

    def V(self) -> int:
        """
        Return number of vertices
        """
        return len(self.edges.keys())

    def vertices(self) -> []:
        """
        Return all the vertices in the graph
        """
        return self.edges.keys()

    def E(self) -> int:
        """
        Return number of edges
        """
        total = 0
        for v in self.edges.keys():
            total += len(self.adj(v))
        return total // 2  # edges are in both direction

    def adj(self, v) -> [Edge]:
        """
        Return edges from vertex v
        """
        if v not in self.edges:
            return []
        return self.edges[v]

    def add_edge(self, e: Edge) -> None:
        """
        Add edge between v and w
        """
        v = e.either()
        w = e.other(v)
        if v not in self.edges:
            self.edges[v] = set()
        if w not in self.edges:
            self.edges[w] = set()
        self.edges[v].add(e)
        self.edges[w].add(e)

    def degree(self, v) -> int:
        return len(self.adj(v))
