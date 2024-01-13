from graphs.undirected_graph import UndirectedGraph


# classic DFS based solution for undirected graph
class Cycle:
    def __init__(self, g: UndirectedGraph):
        self.g = g
        self.visited = set()
        self.has_cycle = False
        for v in g.vertices():
            if v not in self.visited:
                self.dfs(v, -1)

    def dfs(self, v, u):
        self.visited.add(v)
        for w in self.g.adj(v):
            if w not in self.visited:
                self.dfs(w, v)
            elif w != u:
                self.has_cycle = True
                return

# TODO add cycle path
