from graphs.graph import Graph


# classic DFS based solution for undirected graph
class Cycle:
    def __init__(self, g: Graph):
        self.g = g
        self.visited = set()
        self.edge_to = dict()
        self.cycle_path = None
        for v in g.vertices():
            if v not in self.visited:
                self.dfs(v, -1)

    def dfs(self, v, u):
        self.visited.add(v)
        for w in self.g.adj(v):
            # already found cycle
            if self.cycle_path is not None:
                return
            if w not in self.visited:
                self.edge_to[w] = v
                self.dfs(w, v)
            elif w != u:
                self.cycle_path = []
                x = v
                while x != w:
                    self.cycle_path.append(x)
                    x = self.edge_to[x]
                self.cycle_path.append(w)
                self.cycle_path.append(v)

    def has_cycle(self):
        return self.cycle_path is not None

    # todo has parallel egdes and has_self_loop
