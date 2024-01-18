class MinPriorityQueue:
    def __init__(self):
        self.n = 0
        self.heap = [None]

    def pop_min(self):
        if self.is_empty():
            raise Exception('queue is empty')
        minimum = self.heap[1]
        self._swap(1, self.n)
        self.n -= 1
        self._sink(1)
        if self.n > 0 and (self.n == (len(self.heap) - 1) // 4):
            self._resize(len(self.heap) // 2)
        assert self._is_min_heap_ordered(1)
        return minimum

    def min(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self.heap[1]  # first element is at 1 index not 0

    def insert(self, key):
        if self.n == len(self.heap) - 1:
            self._resize(2 * len(self.heap))
        self.n += 1
        self.heap[self.n] = key
        self._swim(self.n)
        assert self._is_min_heap_ordered(1)

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

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

    def _resize(self, capacity):
        assert capacity > 0
        new_heap = [None] * (capacity + 1)
        for i in range(0, self.n + 1):
            new_heap[i] = self.heap[i]
        self.heap = new_heap

    def _assert_is_min_heap(self):
        pass

    def _greater(self, i, j):
        return self.heap[i] > self.heap[j]

    def _swap(self, i, j):
        t = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = t

    def _is_min_heap_ordered(self, k):
        if k > self.n:
            return True
        left = 2 * k
        right = 2 * k + 1
        if left <= self.n and self._greater(k, left):
            return False
        if right <= self.n and self._greater(k, right):
            return False
        return self._is_min_heap_ordered(left) and self._is_min_heap_ordered(right)
