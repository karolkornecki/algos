# linear probing/open addressing collision resolution strategy


class LinearProbingST:
    SIZE = 1001

    def __init__(self):
        self.key = [None for _ in range(LinearProbingST.SIZE)]
        self.value = [None for _ in range(LinearProbingST.SIZE)]
        self.size = 0

    def insert(self, key, value):
        i = self.i(key)
        pos = i
        while self.key[pos] is not None:
            if self.key[pos] == key:
                self.value[pos] = value
                return
            pos = (pos + 1) % LinearProbingST.SIZE
        self.key[pos] = key
        self.value[pos] = value
        self.size += 1

    def get(self, key):
        i = self.i(key)
        pos = i
        while self.key[pos] is not None:
            if self.key[pos] == key:
                return self.value[pos]
        return None

    def delete(self, key):
        i = self.i(key)
        pos = i
        while self.key[pos] is not None:
            if self.key[pos] == key:
                self.key[pos] = None
                self.value[pos] = None
                self.size -= 1

    def i(self, key):
        return hash(key) % LinearProbingST.SIZE

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
