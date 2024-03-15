from graphs.digraph import Digraph


class DirectedCycle:
    def __init__(self, g: Digraph):
        self.g = g
        self.visited = set()
        self.edge_to = dict()
        self.on_stack = set()
        self.has_cycle = False

        for v in g.vertices:
            if v not in self.visited:
                self.dfs(v)

    def dfs(self, v):
        self.visited.add(v)
        self.on_stack.add(v)
        for w in self.g.adj(v):
            if self.has_cycle:
                return
            elif w not in self.visited:
                self.dfs(w)
            elif w in self.on_stack:
                self.has_cycle = True
        self.on_stack.remove(v)
