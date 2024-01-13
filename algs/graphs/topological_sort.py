# topological sort - reverse DFS postorder
from graphs.digraph import Digraph


def topological_sort(g: Digraph):
    # g cannot have cycles
    postorder_stack = []
    visited = set()
    for v in g.vertices():
        if v not in visited:
            dfs(g, v, postorder_stack, visited)
    return list(reversed(postorder_stack))


def dfs(g, v, s, visited):
    visited.add(v)
    for w in g.adj(v):
        if w not in visited:
            dfs(g, w, s, visited)
    s.append(v)
