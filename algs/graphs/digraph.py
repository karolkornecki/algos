from graphs.graph import Graph


class Digraph(Graph):
    """
    Directed Graph
    """

    def __init__(self):
        self.edges = dict()

    def v(self) -> int:
        return len(self.edges.keys())

    def vertices(self) -> []:
        return self.edges.keys()

    def e(self) -> int:
        total = 0
        for key in self.edges.keys():
            total += len(self.adj(key))
        return total

    def adj(self, v) -> [int]:
        if v not in self.edges:
            return []
        return self.edges[v]

    def add_edge(self, v: int, w: int) -> None:
        if v not in self.edges:
            self.edges[v] = []
        self.edges[v].append(w)
