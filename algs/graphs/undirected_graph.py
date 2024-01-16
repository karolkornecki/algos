class Graph:
    """
    Undirected Graph
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
        for key in self.edges.keys():
            total += len(self.adj(key))
        return total // 2  # edges are in both direction

    def adj(self, v) -> [int]:
        """
        Return edges from vertex v
        """
        if v not in self.edges:
            return []
        return self.edges[v]

    def add_edge(self, v: int, w: int) -> None:
        """
        Add edge between v and w
        """
        if v not in self.edges:
            self.edges[v] = []
        if w not in self.edges:
            self.edges[w] = []
        self.edges[v].append(w)
        self.edges[w].append(v)

    def degree(self, v) -> int:
        return len(self.adj(v))
