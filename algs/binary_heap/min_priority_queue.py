class MinPriorityQueue:
    def __init__(self):
        self.n = 0
        self.heap = [None]

    def pop_min(self):
        if self.is_empty():
            raise Exception('queue is empty')
        minimum = self.heap[1]
        self.swap(1, self.n)
        self.n -= 1
        self.sink(1)
        if self.n > 0 and (self.n == (len(self.heap) - 1) // 4):
            self.resize(len(self.heap) // 2)
        assert self.is_min_heap_ordered(1)
        return minimum

    def min(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self.heap[1]  # first element is at 1 index not 0

    def insert(self, key):
        if self.n == len(self.heap) - 1:
            self.resize(2 * len(self.heap))
        self.n += 1
        self.heap[self.n] = key
        self.swim(self.n)
        assert self.is_min_heap_ordered(1)

    def size(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.greater(j, j + 1):
                j += 1
            if not self.greater(k, j):
                break
            self.swap(k, j)
            k = j

    def swim(self, k):
        while k > 1 and self.greater(k // 2, k):
            self.swap(k // 2, k)
            k = k // 2

    def resize(self, capacity):
        assert capacity > 0
        new_heap = [None] * (capacity + 1)
        for i in range(0, self.n + 1):
            new_heap[i] = self.heap[i]
        self.heap = new_heap

    def assert_is_min_heap(self):
        pass

    def greater(self, i, j):
        return self.heap[i] > self.heap[j]

    def swap(self, i, j):
        t = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = t

    def is_min_heap_ordered(self, k):
        if k > self.n:
            return True
        left = 2 * k
        right = 2 * k + 1
        if left <= self.n and self.greater(k, left):
            return False
        if right <= self.n and self.greater(k, right):
            return False
        return self.is_min_heap_ordered(left) and self.is_min_heap_ordered(right)
