from undirected_graph import Graph


def dfs(g: Graph):
    visited = set()
    _dfs(g, 0, visited)


def _dfs(g, v, visited):
    visited.add(v)
    print(v)
    for w in g.adj(v):
        if w not in visited:
            _dfs(g, w, visited)


def dfs_iter(g: Graph):
    visited = set()
    start = 0
    stack = [start]
    visited.add(start)
    while stack:
        v = stack.pop()
        print(v)
        for w in g.adj(v):
            if w not in visited:
                stack.append(w)
                visited.add(w)


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
    dfs(g)
    print()
    dfs_iter(g)
