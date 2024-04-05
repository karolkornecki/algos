from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        partition_sum = sum(nums) / 2

        @cache
        def dp(target, current_num):
            # hit the target
            if target == 0:
                return True
            # missed the target
            if target < 0:
                return False
            # out of numbers in the set
            if current_num >= n:
                return False
            # can hit target using current num or not using current num ?
            return dp(target - nums[current_num], current_num + 1) or dp(target, current_num + 1)

        return dp(partition_sum, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.canPartition([1, 5, 11, 5])
    assert not s.canPartition([1, 2, 3, 5])
    assert not s.canPartition(
        [83, 12, 15, 68, 83, 71, 72, 99, 66, 75, 53, 74, 30, 65, 95, 40, 22, 4, 67, 61, 55, 63, 85, 81, 67, 10, 93, 24,
         24, 43, 29, 88, 94, 97, 27, 87, 51, 12, 26, 47, 10, 21, 16, 2, 8, 20, 94, 19, 66, 6, 13, 68, 27, 45, 90, 20,
         47, 53, 71, 89, 75, 88, 88, 92, 12, 85, 22, 74, 82, 38, 2, 74, 21, 16, 29, 9, 9, 24, 23, 76, 24, 70, 64, 89,
         78, 84, 76, 84, 95, 9, 75, 62, 94, 84, 48, 57, 82, 26, 47, 95])
