from collections import defaultdict
from typing import List


# DP - bottom up
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points_by_num = defaultdict(int)
        max_num = 0
        for n in nums:
            points_by_num[n] += n
            max_num = max(max_num, n)

        dp = defaultdict(int)
        dp[0] = 0
        dp[1] = points_by_num[1]
        for n in range(2, max_num + 1):
            dp[n] = max(points_by_num[n] + dp[n - 2], dp[n - 1])
        return dp[max_num]


# DP - top down -> accepted
class Solution3:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def max_points(x, nums, dp) -> int:
            if x in dp:
                return dp[x]
            if x == 0:
                return 0
            if x == 1:
                return nums[1]
            dp[x] = max(nums[x] + max_points(x - 2, nums, dp), max_points(x - 1, nums, dp))
            return dp[x]

        dp = {}
        points_by_num = defaultdict(int)
        max_num = 0
        for n in nums:
            points_by_num[n] += n
            max_num = max(max_num, n)
        return max_points(max_num, points_by_num, dp)


# recurrence by still TLE
class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # max point we can get from 0 up to x
        def max_points(x, nums) -> int:
            if x == 0:
                return 0
            if x == 1:
                return nums[1]
            return max(nums[x] + max_points(x - 2, nums), max_points(x - 1, nums))

        points_by_num = defaultdict(int)
        max_num = 0
        for n in nums:
            points_by_num[n] += 1
            max_num = max(max_num, n)
        for k in points_by_num:
            points_by_num[k] *= k
        return max_points(max_num, points_by_num)


# straightforward recursive solution
# Time Limit Exceeded
class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        m = 0
        for i in range(len(nums)):
            m = max(m, nums[i] + self.deleteAndEarn(rest(i, nums.copy())))
        return m


def rest(i, nums):
    n = []
    for j in range(len(nums)):
        if j == i:
            continue
        if nums[j] == nums[i] - 1:
            continue
        if nums[j] == nums[i] + 1:
            continue
        n.append(nums[j])
    return n


if __name__ == "__main__":
    s = Solution()
    assert s.deleteAndEarn([3, 4, 2]) == 6
    assert s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
    assert s.deleteAndEarn([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4]) == 61
    assert s.deleteAndEarn(
        [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91,
         85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13,
         60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1,
         90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]) == 3451
