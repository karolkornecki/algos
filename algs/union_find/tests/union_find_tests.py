import unittest

from union_find import quick_find_uf as qf, quick_union_uf as qu, weighted_quick_union_uf as wqu, \
    quick_union_path_compression_uf as qupc, weighted_quick_union_path_compression_uf as wqupc


# algorithm | worst-case time
# quick-find | M*N
# quick-union | M*N
# weighted QU | N + M*log*N
# QU + path compression | N + M*logN
# weighted QU + path compression | N + M*logN <---- the best option in practice it's linear time in the worst-case
class UnionFindTestCase(unittest.TestCase):
    def test_quick_find_uf(self):
        union_find = qf.QuickFindUF(5)
        union_find.union(0, 1)
        union_find.union(1, 2)
        self.assertEqual(True, union_find.connected(0, 1))
        self.assertEqual(True, union_find.connected(0, 2))
        self.assertEqual(True, union_find.connected(1, 2))
        self.assertEqual(False, union_find.connected(1, 3))

    def test_quick_union_uf(self):
        union_find = qu.QuickUnionUF(5)
        union_find.union(0, 1)
        union_find.union(1, 2)
        self.assertEqual(True, union_find.connected(0, 1))
        self.assertEqual(True, union_find.connected(0, 2))
        self.assertEqual(True, union_find.connected(1, 2))
        self.assertEqual(False, union_find.connected(1, 3))

    def test_weighted_quick_union_uf(self):
        union_find = wqu.WeightedQuickUnionUF(10)
        # 0,1,2,3,4
        union_find.union(0, 1)
        union_find.union(1, 2)
        union_find.union(2, 3)
        union_find.union(3, 4)
        self.assertEqual(0, union_find.root(0))
        self.assertEqual(0, union_find.root(1))
        self.assertEqual(0, union_find.root(2))
        self.assertEqual(0, union_find.root(3))
        self.assertEqual(0, union_find.root(4))
        self.assertEqual(5, union_find.size[union_find.root(0)])  # root any of first connected component element eg.: 0

        # another connected component
        union_find.union(5, 6)
        union_find.union(6, 7)
        self.assertEqual(5, union_find.root(5))
        self.assertEqual(5, union_find.root(6))
        self.assertEqual(5, union_find.root(7))
        self.assertEqual(3, union_find.size[union_find.root(6)])  # root any of first connected component element eg.: 6

        # join two components
        union_find.union(2, 6)
        # then assert that smaller (in the number of nodes) component was merged to larger one
        self.assertEqual(0, union_find.root(5))
        self.assertEqual(0, union_find.root(6))
        self.assertEqual(0, union_find.root(7))
        # and size increased
        self.assertEqual(8, union_find.size[union_find.root(6)])

    def test_quick_union_path_compression_uf(self):
        union_find = qupc.QuickUnionPathCompressionUF(5)
        union_find.union(0, 1)
        union_find.union(1, 2)
        self.assertEqual(True, union_find.connected(0, 1))
        self.assertEqual(True, union_find.connected(0, 2))
        self.assertEqual(True, union_find.connected(1, 2))
        self.assertEqual(False, union_find.connected(1, 3))

    def test_weighted_quick_union_path_compression_uf(self):
        union_find = wqupc.WeightedQuickUnionPathCompressionUF(10)
        # 0,1,2,3,4
        union_find.union(0, 1)
        union_find.union(1, 2)
        union_find.union(2, 3)
        union_find.union(3, 4)
        self.assertEqual(0, union_find.root(0))
        self.assertEqual(0, union_find.root(1))
        self.assertEqual(0, union_find.root(2))
        self.assertEqual(0, union_find.root(3))
        self.assertEqual(0, union_find.root(4))
        self.assertEqual(5, union_find.size[union_find.root(0)])  # root any of first connected component element eg.: 0

        # another connected component
        union_find.union(5, 6)
        union_find.union(6, 7)
        self.assertEqual(5, union_find.root(5))
        self.assertEqual(5, union_find.root(6))
        self.assertEqual(5, union_find.root(7))
        self.assertEqual(3, union_find.size[union_find.root(6)])  # root any of first connected component element eg.: 6

        # join two components
        union_find.union(2, 6)
        # then assert that smaller (in the number of nodes) component was merged to larger one
        self.assertEqual(0, union_find.root(5))
        self.assertEqual(0, union_find.root(6))
        self.assertEqual(0, union_find.root(7))
        # and size increased
        self.assertEqual(8, union_find.size[union_find.root(6)])


if __name__ == '__main__':
    unittest.main()
