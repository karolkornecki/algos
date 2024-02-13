from heapq import heappush, heappop
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = dict()
        for e in edges:
            src, dest, cost = e
            if src not in self.edges:
                self.edges[src] = set()
            self.edges[src].add((dest, cost))

    def addEdge(self, edge: List[int]) -> None:
        src, dest, cost = edge
        if src not in self.edges:
            self.edges[src] = set()
        self.edges[src].add((dest, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = []
        dist = dict()
        for v in range(self.n):
            dist[v] = -1
        dist[node1] = 0
        heappush(pq, (dist[node1], node1))
        while pq:
            v_cost, v = heappop(pq)
            if v == node2:
                return dist[node2]
            if v not in self.edges:
                continue
            for e in self.edges[v]:
                w, w_cost = e
                if dist[w] == -1 or dist[w] > dist[v] + w_cost:
                    dist[w] = dist[v] + w_cost
                    heappush(pq, (dist[w], w))
        return dist[node2]


if __name__ == '__main__':
    g = Graph(13, [[7, 2, 131570], [9, 4, 622890], [9, 1, 812365], [1, 3, 399349], [10, 2, 407736], [6, 7, 880509],
                   [1, 4, 289656], [8, 0, 802664], [6, 4, 826732], [10, 3, 567982], [5, 6, 434340], [4, 7, 833968],
                   [12, 1, 578047], [8, 5, 739814], [10, 9, 648073], [1, 6, 679167], [3, 6, 933017], [0, 10, 399226],
                   [1, 11, 915959], [0, 12, 393037], [11, 5, 811057], [6, 2, 100832], [5, 1, 731872], [3, 8, 741455],
                   [2, 9, 835397], [7, 0, 516610], [11, 8, 680504], [3, 11, 455056], [1, 0, 252721]])
    print(g.shortestPath(9, 3))
    g.addEdge([11, 1, 873094])
    print(g.shortestPath(3, 10))
