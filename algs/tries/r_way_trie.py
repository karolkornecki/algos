R = 26


# simple 26-way-trie
# not appropriate for large dictionary due to memory overhead
class Trie:
    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word):
        if word is None or len(word) == 0:
            return
        self._insert(self.root, word, 0)

    def _insert(self, n, word, d):
        c = i(word[d])
        if n.next[c] is None:
            n.next[c] = Trie.Node()
        if d == len(word) - 1:
            n.next[c].word = True
            return
        self._insert(n.next[c], word, d + 1)

    def search(self, word):
        if word is None or len(word) == 0:
            return False
        return self._search(self.root, word, 0)

    def _search(self, n, word, d):
        c = i(word[d])
        if n.next[c] is None:
            return False
        elif d == len(word) - 1:
            return n.next[c].word
        else:
            return self._search(n.next[c], word, d + 1)

    # TODO prefix and keys methods -> like in TST
    class Node:
        def __init__(self):
            self.next = [None for _ in range(R)]
            self.word = False


def i(ch) -> int:
    return ord(ch) - ord('a')
