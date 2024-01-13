from graphs.digraph import Digraph
from graphs.topological_sort import topological_sort


# Kosaraju-Sharir algorithm for strongly connected components.
# SCC - connected component where if there is a path from v -> w then need to be a path from w -> v as well.
def scc(g: Digraph):
    # compute reverse postorder of reverse graph
    reverse_post_order = topological_sort(g.reverse())
    visited = set()
    component_id = dict()
    count = 0
    for v in reverse_post_order:
        if v not in visited:
            dfs(g, v, visited, component_id, count)
            count += 1
    return count, component_id


def dfs(g, v, visited, component_id, count):
    visited.add(v)
    component_id[v] = count
    for w in g.adj(v):
        if w not in visited:
            dfs(g, w, visited, component_id, count)
