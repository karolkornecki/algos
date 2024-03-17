from typing import List


# DP bottom up - memory optimized
class Solution5:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            current = max(nums[i] + prev_prev, prev)
            prev_prev = prev
            prev = current
        return prev


# DP bottom up
class Solution4:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[len(nums) - 1]


# DP - top down
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = dict()
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        return self._rob(len(nums) - 1, nums, dp)

    def _rob(self, i, nums: List[int], dp) -> int:
        if i in dp:
            return dp[i]
        dp[i] = max(nums[i] + self._rob(i - 2, nums, dp), self._rob(i - 1, nums, dp))
        return dp[i]


# recurrence - same as below but with indexes instead of slicing arrays
# Time Limit Exceeded
class Solution2:
    def rob(self, nums: List[int]) -> int:
        return self._rob(len(nums) - 1, nums)

    def _rob(self, i, nums: List[int]) -> int:
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        return max(nums[i] + self._rob(i - 2, nums), self._rob(i - 1, nums))


# recurrence
# Time Limit Exceeded
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(nums[-1] + self.rob(nums[:len(nums) - 2]), self.rob(nums[:len(nums) - 1]))


if __name__ == "__main__":
    s = Solution5()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
