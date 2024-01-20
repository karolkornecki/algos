from graphs.edge_weighted_digraph import EdgeWeightedDigraph


class EdgeWeightedDirectedCycle:
    def __init__(self, g: EdgeWeightedDigraph):
        self.visited = set()
        self.on_stack = set()
        self.edge_to = dict()
        self.cycle = []
        for v in g.vertices():
            if v not in self.visited:
                self._dfs(g, v)

    def _dfs(self, g: EdgeWeightedDigraph, v):
        self.on_stack.add(v)
        self.visited.add(v)
        for edge in g.adj(v):
            if len(self.cycle) > 0:
                return

            w = edge.dest()
            if w not in self.visited:
                self.edge_to[w] = edge
                self._dfs(g, w)
            elif w in self.on_stack:
                f = edge
                while f.src() != w:
                    self.cycle.append(f)
                    f = self.edge_to[f.src()]
                self.cycle.append(f)
                return

        self.on_stack.remove(v)
