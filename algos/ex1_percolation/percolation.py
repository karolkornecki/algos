import random

import numpy as np

from union_find import weighted_quick_union_uf as uf


class Percolation:
    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n):
        if n < 0:
            raise Exception()
        self.n = n
        self.number_of_opened = 0
        self.uf = uf.WeightedQuickUnionUF(n ** 2)
        self.optimized = uf.WeightedQuickUnionUF(n ** 2 + 2)

        # artificial node for optimization
        for column in range(1, n + 1):
            self.optimized.union(0, column)
            self.optimized.union(n ** 2 + 1, n ** 2 + 1 - column)

        self.grid = [[False for _ in range(n)] for _ in range(n)]

    # opens the site (row, col) if it is not open already
    def open(self, row, col):
        if self.is_open(row, col):
            return
        row, col = self.validate_and_normalize(row, col)
        self.grid[row][col] = True
        self.number_of_opened += 1
        for r, c in self.neighbours(row, col):
            if self.is_open(r + 1, c + 1):
                self.uf.union(self.to_index(row, col), self.to_index(r, c))
                self.optimized.union(self.to_optimized_index(row, col), self.to_optimized_index(r, c))

    # is the site (row, col) open?
    def is_open(self, row, col):
        row, col = self.validate_and_normalize(row, col)
        return self.grid[row][col]

    # is the site (row, col) full?
    def is_full(self, row, col):
        if not self.is_open(row, col):
            return False
        row, col = self.validate_and_normalize(row, col)
        return self.optimized.connected(0, self.to_optimized_index(row, col))

    # returns the number of open sites
    def number_of_open_sites(self):
        return self.number_of_opened

    # does the system percolate?
    def percolates(self):
        if self.number_of_open_sites() == 0:
            return False
        # if two artificial nodes are connected ten percolates
        return self.optimized.connected(0, self.n ** 2 + 1)

    def validate_and_normalize(self, row, col):
        if row < 1 or row > self.n or col < 1 or col > self.n:
            raise Exception()
        return row - 1, col - 1

    def neighbours(self, row, col):
        return list(filter(lambda point: self.in_range(*point),
                           [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]))

    def in_range(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n

    def to_index(self, row, col):
        return row * self.n + col

    def to_optimized_index(self, row, col):
        return row * self.n + col + 1


class PercolationStats:
    # perform independent trials on an n-by-n grid
    def __init__(self, n, trials):
        if n <= 0 or trials <= 0:
            raise Exception()
        self.n = n
        self.trials = trials
        self.results = []
        self.o = 0
        self.ok = 0
        for i in range(trials):
            self.do_experiment(n)

    def do_experiment(self, n):
        p = Percolation(n)
        while True:
            r = random.randint(1, n)
            c = random.randint(1, n)
            if not p.is_open(r, c):
                p.open(r, c)
                self.ok +=1
                if p.percolates():
                    break
            else:
                self.o += 1
        self.results.append(p.number_of_open_sites())

    # sample mean of percolation threshold
    def mean(self):
        return np.mean(self.results) / self.n ** 2

    # sample standard deviation of percolation threshold
    def stddev(self):
        return np.std(self.results) / self.n ** 2

    # low endpoint of 95% confidence interval
    def confidence_lo(self):
        return self.mean() - ((1.96 * self.stddev()) / np.sqrt(self.trials))

    # high endpoint of 95% confidence interval
    def confidence_hi(self):
        return self.mean() + ((1.96 * self.stddev()) / np.sqrt(self.trials))

    def show(self):
        print(f'mean                    = {self.mean()}')
        print(f'stddev                  = {self.stddev()}')
        print(f'95% confidence interval = [{self.confidence_lo()}, {self.confidence_hi()}]')


if __name__ == '__main__':
    p1 = PercolationStats(200, 100)
    p1.show()
    p2 = PercolationStats(2, 10000)
    p2.show()
