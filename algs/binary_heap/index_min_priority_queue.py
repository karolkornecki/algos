class IndexMinPriorityQueue:
    def __init__(self):
        # initial capacity of pq
        self.capacity = 100
        # size of pq
        self.n = 0
        # binary heap using 1 based indexing
        self.pq = [-1 for _ in range(self.capacity + 1)]
        # inverse of pq - qp[pq[i]] = pq[qp[i]] = i
        self.qp = [-1 for _ in range(self.capacity + 1)]
        # priority of i
        self.keys = [None for _ in range(self.capacity + 1)]

    def is_empty(self) -> bool:
        return self.n == 0

    def contains(self, index):
        """ Is this index in pq"""
        return self.qp[index] != -1

    def size(self):
        return self.n

    def insert(self, index, key):
        self._validate_index(index)
        if self.contains(index):
            raise Exception('index already exist in pq')
        self.n += 1
        self.qp[index] = self.n
        self.pq[self.n] = index
        self.keys[index] = key
        self._swim(self.n)

    def min_index(self):
        if self.n == 0:
            raise Exception('pq is empty')
        return self.pq[1]

    def min_key(self):
        if self.n == 0:
            raise Exception('pq is empty')
        return self.keys[self.pq[1]]

    def del_min(self):
        """Delete min key and return its index"""
        if self.n == 0:
            raise Exception('pq is empty')
        min_index = self.pq[1]
        self.n -= 1
        self._swap(1, self.n)
        self._sink(1)
        assert min_index == self.pq[self.n + 1]
        self.qp[min_index] = -1
        self.keys[min_index] = None
        self.pq[self.n + 1] = -1
        return min_index

    def key_of(self, index):
        self._validate_index(index)
        if not self.contains(index):
            raise Exception('index does not exist in pq')
        return self.keys[index]

    def change_key(self, index, key):
        self._validate_index(index)
        if not self.contains(index):
            raise Exception('index does not exist in pq')
        self.keys[index] = key
        self._swim(self.qp[index])
        self._sink(self.qp[index])

    def decrease_key(self, index, key):
        self._validate_index(index)
        if not self.contains(index):
            raise Exception('index does not exist in pq')
        if self.keys[index] == key:
            raise Exception('[decrease_key] key is equal to the key in pq')
        if self.keys[index] < key:
            raise Exception('[decrease_key] key in pq is less than the key')
        self.keys[index] = key
        self._swim(self.qp[index])

    def increase_key(self, index, key):
        self._validate_index(index)
        if not self.contains(index):
            raise Exception('index does not exist in pq')
        if self.keys[index] == key:
            raise Exception('[increase_key] key is equal to the key in pq')
        if self.keys[index] > key:
            raise Exception('[increase_key] key in pq is greater than the key')
        self.keys[index] = key
        self._sink(self.qp[index])

    def delete(self, index):
        self._validate_index(index)
        if not self.contains(index):
            raise Exception('index does not exist in pq')
        i = self.qp[index]
        self.n -= 1
        self._swap(i, self.n)
        self._swim(i)
        self._sink(i)
        self.keys[index] = None
        self.qp[index] = -1

    def _swap(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def _greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def _sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self._greater(j, j + 1):
                j += 1
            if not self._greater(k, j):
                break
            self._swap(k, j)
            k = j

    def _swim(self, k):
        while k > 1 and self._greater(k // 2, k):
            self._swap(k // 2, k)
            k = k // 2

    def _validate_index(self, i):
        if i < 0:
            raise Exception('invalid index')
