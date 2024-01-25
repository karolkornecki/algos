R = 26


# simple 26-way-trie
# not appropriate for large dictionary due to memory overhead
class Trie:
    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word):
        if word is None or len(word) == 0:
            return
        self._insert(self.root.nodes, word)

    def _insert(self, nodes, word):
        c = i(word[0])
        if nodes[c] is None:
            nodes[c] = Trie.Node()
        if len(word) == 1:
            nodes[c].word = True
            return
        self._insert(nodes[c].nodes, word[1:])

    def search(self, word):
        if word is None or len(word) == 0:
            return False
        return self._search(self.root.nodes, word)

    def _search(self, nodes, word):
        c = i(word[0])
        if nodes[c] is None:
            return False
        elif len(word) == 1:
            return nodes[c].word
        else:
            return self._search(nodes[c].nodes, word[1:])

    class Node:
        def __init__(self):
            self.nodes = [None for _ in range(R)]
            self.word = False


def i(ch) -> int:
    return ord(ch) - ord('a')
