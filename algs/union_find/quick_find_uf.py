class QuickFindUF:
    #   Quick-find defect:
    # ・Union too expensive (N array accesses).
    # ・Trees are flat, but too expensive to keep them flat
    # algorithm initialize union find
    # quick-find N N 1
    def __init__(self, n):
        self.id = [i for i in range(n)]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    # Union is too expensive. It takes N^2 array accesses to process a sequence of
    # N union commands on N objects.
    def union(self, p, q):
        p_parent = self.id[p]
        q_parent = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == p_parent:
                self.id[i] = q_parent
