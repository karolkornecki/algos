# red-black bst is self balanced binary tree (works similarly to 2-3-tree, but it's easier to implement)
# that guarantee LogN complexity performance of operations: insert, get, delete

class RedBlackBST:
    BLACK = False
    RED = True

    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == RedBlackBST.RED

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
        self.root.color = RedBlackBST.BLACK

    def _put(self, node, key, value):
        if node is None:
            return RedBlackBST.TreeNode(key, value, RedBlackBST.RED, 1)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        # fix-up any right-leaning links
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def del_min(self):
        if self.is_empty():
            raise Exception('tree is empty')
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RedBlackBST.RED
        self.root = self._del_min(self.root)
        if not self.is_empty():
            self.root.color = RedBlackBST.BLACK

    def _del_min(self, node):
        if node.left is None:
            return None  # ?node.right?
        if not self.is_red(node.left) and not self.is_red(node.left.left):
            node = self.move_red_left(node)

        node.left = self._del_min(node.left)
        return self.balance(node)

    def delete(self, key):
        if key is None:
            raise Exception('key is none')
        if not self.contains(key):
            return
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RedBlackBST.RED
        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = RedBlackBST.BLACK

    def _delete(self, node, key):
        if key < node.key:
            if not self.is_red(node.left) and not self.is_red(node.left.left):
                node = self.move_red_left(node)
                node.left = self._delete(node.left, key)
        else:
            if self.is_red(node.left):
                node = self.rotate_right(node)
            if key == node.key and node.right is None:
                return None
            if not self.is_red(node.right) and not self.is_red(node.right.left):
                node = self.move_red_right(node)
            if key == node.key:
                x = self._min(node.right)
                node.key = x.key
                node.value = x.value
                node.right = self._del_min(node.right)
            else:
                node.right = self._delete(node.right, key)
        return self.balance(node)

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RedBlackBST.RED
        x.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return x

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RedBlackBST.RED
        x.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return x

    def flip_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = node.right.color

    def move_red_left(self, node):
        self.flip_colors(node)
        if self.is_red(node.right.left):
            node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
            self.flip_colors(node)
        return node

    def move_red_right(self, node):
        self.flip_colors(node)
        if self.is_red(node.left.left):
            node = self.rotate_right(node)
            self.flip_colors(node)
        return node

    def balance(self, node):
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0  # ?? -1 ??
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
        def __init__(self, key, value, color, size=1):
            self.left = None
            self.right = None
            self.key = key
            self.value = value
            self.size = size
            self.color = color
