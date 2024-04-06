from functools import cache
from typing import List


# DP top-down
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        inf = int(1e9)

        @cache
        def dp(current, two_prev_1, one_prev_1, two_prev_2, one_prev_2):
            if two_prev_1 >= one_prev_1 or two_prev_2 >= one_prev_2:
                return inf
            if current >= n:
                return 0

            # no swap
            no = dp(current + 1, one_prev_1, nums1[current], one_prev_2, nums2[current])

            # swap that's why +1 need to be added
            yes = dp(current + 1, one_prev_1, nums2[current], one_prev_2, nums1[current]) + 1
            return min(no, yes)

        return min(
            dp(2, nums1[0], nums1[1], nums2[0], nums2[1]),
            1 + dp(2, nums1[0], nums2[1], nums2[0], nums1[1]),
            1 + dp(2, nums2[0], nums1[1], nums1[0], nums2[1]),
            2 + dp(2, nums2[0], nums2[1], nums1[0], nums1[1])
        )


if __name__ == "__main__":
    s = Solution()
    assert s.minSwap([1, 2, 3, 8], [5, 6, 7, 4]) == 1
    assert s.minSwap([1, 2, 3, 4], [5, 6, 7, 9]) == 0
    assert s.minSwap([1, 7], [4, 2]) == 1
    assert s.minSwap([0, 3, 5, 8, 9], [2, 1, 4, 6, 9]) == 1
    assert s.minSwap([3, 3, 8, 9, 10], [1, 7, 4, 6, 8]) == 1
    assert s.minSwap([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]) == 1
