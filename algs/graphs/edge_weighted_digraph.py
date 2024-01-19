from graphs.directed_edge import DirectedEdge


class EdgeWeightedDigraph:
    """
    Edge Weighted Directed Graph
    """

    def __init__(self):
        self.edges_dict = dict()

    def V(self) -> int:
        """
        Return number of vertices
        """
        return len(self.vertices())

    def vertices(self) -> []:
        """
        Return all the vertices in the graph
        """
        vertices = set()
        for v in self.edges_dict.keys():
            for e in self.adj(v):
                vertices.add(e.src())
                vertices.add(e.dest())
        return vertices

    def E(self) -> int:
        """
        Return number of edges
        """
        total = 0
        for v in self.edges_dict.keys():
            total += len(self.adj(v))
        return total

    def adj(self, v) -> [DirectedEdge]:
        """
        Return edges from vertex v
        """
        if v not in self.edges_dict:
            return []
        return self.edges_dict[v]

    def add_edge(self, e: DirectedEdge) -> None:
        """
        Add edge between v and w
        """
        v = e.src()
        if v not in self.edges_dict:
            self.edges_dict[v] = set()
        self.edges_dict[v].add(e)

    def degree(self, v) -> int:
        return len(self.adj(v))

    def edges(self) -> [DirectedEdge]:
        edges = set()
        for v in self.edges_dict.keys():
            for e in self.adj(v):
                edges.add(e)
        return edges
