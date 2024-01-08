class BST:
    """
    Symbol table implementation as binary search tree
    """

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    def is_empty(self):
        return self._size(self.root) == 0

    def get(self, key):
        if key is None:
            raise Exception('key is None')
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node.value
        if key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def contains(self, key):
        if key is None:
            raise Exception('key is None')
        return self.get(key) is not None

    def put(self, key, value):
        if key is None:
            raise Exception('key is None')
        if value is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return BST.TreeNode(key, value, 1)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def del_min(self):
        if self.is_empty():
            raise Exception('tree is empty')
        self.root = self._del_min(self.root)

    def _del_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._del_min(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    # https://mathcenter.oxford.emory.edu/site/cs171/hibbardDeletion/
    def delete(self, key):
        if key is None:
            raise Exception('key is none')
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            t = node
            node = self._min(t.right)
            node.right = self._del_min(t.right)
            node.left = t.left
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def min(self):
        if self.is_empty():
            raise Exception('tree is empty')
        return self._min(self.root).key

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def rank(self, key):
        """
        Returns number of nodes strictly less than the key
        """
        if key is None:
            raise Exception('key is None')
        return self._rank(key, self.root)

    def _rank(self, key, node):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def is_bst(self):
        return self._is_bst(self.root, None, None)

    def _is_bst(self, node, lo, hi):
        if node is None:
            return True
        if (lo is not None and node.key <= lo) or (hi is not None and node.key >= hi):
            return False
        return self._is_bst(node.left, lo, node.key) and self._is_bst(node.right, node.key, hi)

    class TreeNode:
        def __init__(self, key, value=None, size=1):
            self.left = None
            self.right = None
            self.key = key
            self.value = value
            self.size = size
