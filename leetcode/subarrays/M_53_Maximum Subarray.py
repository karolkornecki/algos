from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        max_so_far = nums[0]
        for n in nums[1:]:
            max_so_far = max(max_so_far + n, n)
            maximum = max(maximum, max_so_far)
        return maximum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-2, 1]))
    print(s.maxSubArray([-1]))
