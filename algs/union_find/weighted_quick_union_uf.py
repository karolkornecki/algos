class WeightedQuickUnionUF:

    # algorithm initialize union connected
    # weighted QU N lgN lgN
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
