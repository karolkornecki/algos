# Is UndirectedGraph bipartite - does the graph is two-colorable ?
from graphs.undirected_graph import Graph


class Bipartite:
    def __init__(self, g: Graph):
        self.g = g
        self.is_bipartite = True
        self.color = dict()
        self.visited = set()
        for v in g.vertices():
            if v not in self.visited:
                self.color[v] = False
                self.dfs(v)

    def dfs(self, v):
        self.visited.add(v)
        for w in self.g.adj(v):
            if w not in self.visited:
                self.color[w] = not self.color[v]
                self.dfs(w)
            elif self.color[w] == self.color[v]:
                self.is_bipartite = False
                return
