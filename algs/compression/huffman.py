from binary_heap.min_priority_queue import MinPriorityQueue

R = 256  # extended ASCII


class Huffman:

    def compress(self, text):
        freq = [0 for _ in range(R)]
        for c in text:
            freq[ord(c)] += 1

        # build Huffman trie
        node = self._build_trie(freq)

        # TODO to finish

    def _build_trie(self, freq):
        pq = MinPriorityQueue()
        for c in range(R):
            if freq[c] > 0:
                pq.insert(Node(chr(c), freq[c], None, None))

        # merge two smallest trees
        while pq.size() > 1:
            left = pq.pop_min()
            right = pq.pop_min()
            parent = Node('\0', left.freq + right.freq, left, right)
            pq.insert(parent)
        return pq.pop_min()


class Node:
    def __init__(self, ch, freq, left, right):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def __cmp__(self, other):
        return self.freq - other.freq
