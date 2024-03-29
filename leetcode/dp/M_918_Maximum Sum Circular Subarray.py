from typing import List

class Solution2:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = nums[0]
        cur_max = nums[0]

        minimum = nums[0]
        cur_min = nums[0]
        total = nums[0]
        for i in range(1, n):
            total += nums[i]

            cur_max = max(cur_max + nums[i], nums[i])
            maximum = max(maximum, cur_max)

            cur_min = min(cur_min + nums[i], nums[i])
            minimum = min(minimum, cur_min)

        if minimum == total:  # the middle subarray is the whole array
            return maximum
        return max(maximum, total - minimum)


# solved using prefix and suffix sum
class Solution1:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max regular subarray sum
        n = len(nums)
        maximum = nums[0]
        cur_max = nums[0]
        for i in range(1, n):
            cur_max = max(cur_max + nums[i], nums[i])
            maximum = max(maximum, cur_max)

        # prefix sum
        prefix = [0 for _ in range(n)]
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # max prefix up to i-th element
        prefix_max = [0 for _ in range(n)]
        prefix_max[0] = prefix[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], prefix[i])

        # suffix sum
        suffix = [0 for _ in range(n)]
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        # max suffix up to i-th element
        suffix_max = [0 for _ in range(n)]
        suffix_max[n - 1] = suffix[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], suffix[i])

        # max sum of non-overlapping prefix and suffix
        for i in range(n - 1):
            cur_max = max(cur_max, prefix_max[i] + suffix_max[i + 1])
            maximum = max(maximum, cur_max)
        return maximum


# brute force max subarray sum of each rotated array
# TLE
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def max_subarray_sum(i) -> int:
            n = nums[i:] + nums[0:i]
            current = n[0]
            maximum = n[0]
            for i in range(1, len(n)):
                current = max(current + n[i], n[i])
                maximum = max(maximum, current)
            return maximum

        result = nums[0]
        for i in range(0, len(nums)):
            m = max_subarray_sum(i)
            result = max(result, m)
        return result


if __name__ == "__main__":
    s = Solution2()
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([3, 5, -2, -11, -3, 5, 25]) == 38
    assert s.maxSubarraySumCircular([-3, -2, -3]) == -2
    assert s.maxSubarraySumCircular([-5, 3, 5]) == 8
    assert s.maxSubarraySumCircular([-7, 1, 2, 7, -2, -5]) == 10
