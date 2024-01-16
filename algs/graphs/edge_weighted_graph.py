from graphs.edge import Edge


class EdgeWeightedGraph:
    """
    Edge Weighted Undirected Graph
    """

    def __init__(self):
        self.edges_dict = dict()

    def V(self) -> int:
        """
        Return number of vertices
        """
        return len(self.edges_dict.keys())

    def vertices(self) -> []:
        """
        Return all the vertices in the graph
        """
        return self.edges_dict.keys()

    def E(self) -> int:
        """
        Return number of edges
        """
        total = 0
        for v in self.edges_dict.keys():
            total += len(self.adj(v))
        return total // 2  # edges are in both direction

    def adj(self, v) -> [Edge]:
        """
        Return edges from vertex v
        """
        if v not in self.edges_dict:
            return []
        return self.edges_dict[v]

    def add_edge(self, e: Edge) -> None:
        """
        Add edge between v and w
        """
        v = e.either()
        w = e.other(v)
        if v not in self.edges_dict:
            self.edges_dict[v] = set()
        if w not in self.edges_dict:
            self.edges_dict[w] = set()
        self.edges_dict[v].add(e)
        self.edges_dict[w].add(e)

    def degree(self, v) -> int:
        return len(self.adj(v))

    def edges(self) -> [Edge]:
        edges = set()  # to get unique edges
        for v in self.edges_dict.keys():
            for e in self.adj(v):
                edges.add(e)
        return edges
