# separate chaining collision resolution strategy


class SeparateChainingST:
    SIZE = 10

    def __init__(self):
        self.a = [[] for _ in range(SeparateChainingST.SIZE)]
        self.size = 0

    def insert(self, key, value):
        i = self.i(key)
        node = SeparateChainingST.Node(key, value)
        for v in self.a[i]:
            if v.key == key:
                v.value = value
                return
        self.a[i].append(node)
        self.size += 1

    def get(self, key):
        i = self.i(key)
        for e in self.a[i]:
            if e.key == key:
                return e.value
        return None

    def delete(self, key):
        i = self.i(key)
        if self.get(key) is not None:
            for at in range(len(self.a[i])):
                if self.a[i][at].key == key:
                    self.a[i].pop(at)
                    self.size -= 1
                    return

    def i(self, key):
        return hash(key) % SeparateChainingST.SIZE

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
