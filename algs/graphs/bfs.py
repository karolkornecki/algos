from undirected_graph import Graph


# BFS computes the shortest path from source to other vertices in terms of number of edges
def bfs(g: Graph):
    visited = set()
    start = 0
    queue = [start]
    visited.add(start)
    while queue:
        v = queue.pop(0)
        print(v)
        for w in g.adj(v):
            if w not in visited:
                queue.append(w)
                visited.add(w)
                # visited must be marked before it's actually processing,
                # because some other nodes may point to it, and they may be duplicated in the queue


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(5, 3)
    g.add_edge(5, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 4)
    bfs(g)
