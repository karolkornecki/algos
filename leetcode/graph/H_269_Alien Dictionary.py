# PREMIUM
from typing import List


class DirectedCycle:
    def __init__(self, g):
        self.g = g
        self.visited = set()
        self.edge_to = dict()
        self.on_stack = set()
        self.has_cycle = False

        for v in g:
            if v not in self.visited:
                self.dfs(v)

    def dfs(self, v):
        self.visited.add(v)
        self.on_stack.add(v)
        for w in self.g[v]:
            if self.has_cycle:
                return
            elif w not in self.visited:
                self.dfs(w)
            elif w in self.on_stack:
                self.has_cycle = True
        self.on_stack.remove(v)


class TopologicalSort:
    def __init__(self, graph):
        self.graph = graph
        self.postorder_stack = []
        visited = set()
        for vertex in graph:
            if vertex not in visited:
                self.dfs(vertex, visited)

    def dfs(self, v, visited):
        visited.add(v)
        if v in self.graph:
            for w in self.graph[v]:
                if w not in visited:
                    self.dfs(w, visited)
        self.postorder_stack.append(v)

    def sorted(self):
        return "".join(list(reversed(self.postorder_stack)))


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = dict()
        for word in words:
            for letter in word:
                graph[letter] = set()

        i = 1
        while i < len(words):
            w1 = words[i - 1]
            w2 = words[i]
            p = 0
            while p < len(w1) and p < len(w2):
                if len(w1) > len(w2) and w1.startswith(w2):
                    return ""
                if w1[p] != w2[p]:
                    graph[w1[p]].add(w2[p])
                    break  # only first
                p += 1
            i += 1

        if DirectedCycle(graph).has_cycle:
            return ""
        return TopologicalSort(graph).sorted()


if __name__ == '__main__':
    s = Solution()
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert s.alienOrder(["z", "x"]) == "zx"
    assert s.alienOrder(["z", "x", "z"]) == ""
    assert s.alienOrder(["zab", "zabc", "a"]) == "cbza"
    assert s.alienOrder(["aac", "aabb", "aaba"]) == "cba"
    assert s.alienOrder(["ac", "ab", "zc", "zb"]) == "cbaz"
    assert s.alienOrder(["a", "b", "ca", "cc"]) == "abc"
    assert s.alienOrder(["ab", "abc"]) == "cba"
    assert s.alienOrder(["abc", "ab"]) == ""
    assert s.alienOrder(["z", "z"]) == "z"
    assert s.alienOrder(["wrt", "wrtkj"]) == "jktrw"
