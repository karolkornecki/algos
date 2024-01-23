from graphs.mincut_maxflow.flow_network import FlowNetwork

INFINITY = 2000000000


# maximum st-flow and minimum st-cut using Ford-Fulkerson algorithm
# value of max-flow == capacity of min-cut
# Works for directed weighted graph
class FordFulkerson:
    def __init__(self, g: FlowNetwork, s, t):
        # assumption s and t are vertices in g and flow is feasible
        if s == t:
            raise Exception('s and t are the same')
        self.visited = set()  # if v is in residual path on s->v then it is added to set
        self.edge_to = dict()  # last edge on s->v
        self.v = 0  # value of the flow

        while self._has_augmenting_path(g, s, t):
            bottleneck = INFINITY

            # compute bottleneck capacity (edge with the smallest capacity along the augmenting path)
            v = t
            while v != s:
                bottleneck = min(bottleneck, self.edge_to[v].residual_capacity_to(v))
                v = self.edge_to[v].other(v)

            # augment flow
            v = t
            while v != s:
                self.edge_to[v].add_residual_flow_to(v, bottleneck)
                v = self.edge_to[v].other(v)

            self.v += bottleneck

    # complexity of this method for maxflow/mincut depends mainly on complexity of finding augmenting path:
    # standard ford-fulkerson method uses DFS
    # Edmond's-Karp algorithm uses BFS - O(E^2*V)
    # Dinic's algorithms uses combination of DFS and BFS - O(V^2*E)
    def _has_augmenting_path(self, g: FlowNetwork, s, t):
        """ checks if there is still a path from s to t with some available capacity"""
        self.visited = set()
        self.edge_to = dict()
        queue = [s]
        self.visited.add(s)
        while queue and t not in self.visited:
            v = queue.pop(0)
            for edge in g.adj(v):
                w = edge.other(v)
                # found path from s to w in the residual network ?
                if edge.residual_capacity_to(w) > 0:
                    if w not in self.visited:
                        # save last edge on path to w
                        self.edge_to[w] = edge
                        self.visited.add(w)
                        queue.append(w)
        # is t reachable from s in the residual network
        return t in self.visited

    def value(self):
        return self.v

    def in_cut(self, v):
        return v in self.visited
