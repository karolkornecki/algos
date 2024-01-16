from graphs.undirected_graph import Graph


def connected_components(g: Graph):
    count = 0
    visited = set()
    component_id = dict()
    for v in g.vertices():
        if v not in visited:
            dfs(g, v, count, component_id, visited)
            count += 1

    return count, component_id


def dfs(g, v, count, component_id, visited):
    visited.add(v)
    stack = [v]
    while stack:
        current_vertex = stack.pop()
        component_id[current_vertex] = count
        for w in g.adj(current_vertex):
            if w not in visited:
                stack.append(w)
                visited.add(w)
