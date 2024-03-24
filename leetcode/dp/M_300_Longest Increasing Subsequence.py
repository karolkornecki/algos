from typing import List


# top-down
# base case -> single char is always sequence = 1
# recurrence relation -> if j < i and num[j] < num[i] then dp[i] = max(dp[0..j]) + 1
# state -> dp[i] is the length of the longest subsequence that ends at i
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(1, len(nums)):
            n = nums[i]
            max_len = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < n:
                    max_len = max(max_len, dp[j])
            dp[i] = max_len + 1
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert s.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3
    assert s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
