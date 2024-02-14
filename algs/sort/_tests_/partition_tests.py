import unittest

from parameterized import parameterized

from sort import quick_sort as qs


class PartitionTestCase(unittest.TestCase):

    def test_partition_1(self):
        # given
        a = [4, 3, 1, 8, 9]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 3, 4, 8, 9], a)

    def test_partition_2(self):
        # given
        a = [4, 3, 1, 8, 9, 2]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([2, 3, 1, 4, 9, 8], a)

    def test_partition_3(self):
        # given
        a = [1, 2, 3, 4, 5]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 2, 3, 4, 5], a)

    def test_partition_4(self):
        # given
        a = [1, 2, 3, 4, 5, 6]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 2, 3, 4, 5, 6], a)

    def test_partition_5(self):
        # given
        a = [5, 4, 3, 2, 1]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 4, 3, 2, 5], a)

    def test_partition_6(self):
        # given
        a = [6, 5, 4, 3, 2, 1]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 5, 4, 3, 2, 6], a)

    # def test_partition_7(self):
    #     # given
    #     a = [4, 4, 4, 4, 4]
    #     # then
    #     qs.partition(a, 0, len(a) - 1)
    #     # then
    #     self.assertEqual([4, 4, 4, 4, 4], a)

    # def test_partition_8(self):
    #     # given
    #     a = [4, 4, 4, 4, 4, 4]
    #     # then
    #     qs.partition(a, 0, len(a) - 1)
    #     # then
    #     self.assertEqual([4, 4, 4, 4, 4, 4], a)

    def test_partition_10(self):
        # given
        a = [1, 2]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 2], a)

    def test_partition_11(self):
        # given
        a = [2, 1]
        # then
        qs.partition(a, 0, len(a) - 1)
        # then
        self.assertEqual([1, 2], a)

    @parameterized.expand([([], []), ([1], [1])])
    def test_partition_9(self, array_to_partition, expected_result):
        # when
        qs.partition(array_to_partition, 0, len(array_to_partition) - 1)
        # then
        self.assertEqual(expected_result, array_to_partition)


if __name__ == '__main__':
    unittest.main()
