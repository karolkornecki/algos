from graphs.graph import Graph


class UndirectedGraph(Graph):
    """
    Undirected Graph
    """

    def __init__(self):
        self.edges = dict()

    def v(self) -> int:
        return len(self.edges.keys())

    def e(self) -> int:
        total = 0
        for key in self.edges.keys():
            total += len(self.adj(key))
        return total // 2  # edges are in both direction

    def adj(self, v) -> [int]:
        return self.edges[v]

    def add_edge(self, v: int, w: int) -> None:
        if v not in self.edges:
            self.edges[v] = []
        if w not in self.edges:
            self.edges[w] = []
        self.edges[v].append(w)
        self.edges[w].append(v)
