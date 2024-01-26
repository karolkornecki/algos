# Ternary Search Trie
# Space efficient trie data structure
class TST:
    def __init__(self):
        self.n = 0
        self.root = None

    def size(self):
        return self.n

    def put(self, word, value):
        if word is None or len(word) == 0:
            return
        if not self.contains(word):
            self.n += 1
        elif value is None:
            self.n -= 1  # delete
        self.root = self._put(self.root, word, value, 0)

    def _put(self, n, word, value, d):
        ch = word[d]
        if n is None:
            n = TST.Node(ch)
            n.ch = ch
        if ch < n.ch:
            n.left = self._put(n.left, word, value, d)
        elif ch > n.ch:
            n.right = self._put(n.right, word, value, d)
        elif d < len(word) - 1:
            n.mid = self._put(n.mid, word, value, d + 1)
        else:
            n.value = value
        return n

    def get(self, word):
        if word is None or len(word) == 0:
            return None
        return self._get(self.root, word, 0)

    def _get(self, n, word, d):
        if n is None:
            return None
        ch = word[d]
        if ch < n.ch:
            return self._get(n.left, word, d)
        if ch > n.ch:
            return self._get(n.right, word, d)
        if d < len(word) - 1:
            return self._get(n.mid, word, d + 1)
        return n.value

    def contains(self, word):
        return self.get(word) is not None

    def delete(self, word):
        self.put(word, None)

    def keys(self):
        r = []
        self._keys(self.root, "", r)
        return r

    def _keys(self, n, k, r):
        if n is None:
            return
        if n.value is not None:
            r.append(k + n.ch)
        self._keys(n.mid, k + n.ch, r)
        self._keys(n.left, k, r)
        self._keys(n.right, k, r)

    def keys_with_prefix(self, prefix):
        pass
        # TODO

    def keys_that_match(self, regexp):
        pass
        # TODO

    def longest_prefix_of(self, start):
        pass
        # TODO

    class Node:
        def __init__(self, ch):
            self.ch = ch
            self.value = None
            self.left = None
            self.mid = None
            self.right = None
