class Digraph:
    """
    Directed Graph
    """

    def __init__(self):
        self.edges = dict()
        self.in_degree = dict()
        # set of vertices
        self.vertices = set()

    def V(self) -> int:
        """
        Return number of vertices
        """
        return len(self.vertices)

    def E(self) -> int:
        """
        Return number of edges
        """
        total = 0
        for v in self.vertices:
            total += len(self.adj(v))
        return total

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
        self.vertices.add(v)
        self.vertices.add(w)
        if v not in self.edges:
            self.edges[v] = []
        self.edges[v].append(w)
        if w not in self.in_degree:
            self.in_degree[w] = 0
        self.in_degree[w] = self.in_degree[w] + 1

    def reverse(self):
        """
        Reverse direction of all the edges and returns new graph
        """
        r = Digraph()
        for v in self.edges.keys():
            for w in self.adj(v):
                r.add_edge(w, v)
        return r

    def add_vertex(self, v):
        self.vertices.add(v)
