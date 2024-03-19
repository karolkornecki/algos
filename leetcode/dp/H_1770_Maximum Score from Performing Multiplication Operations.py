from typing import List

inf = -1e9


# DP - bottom up -> time ~800ms
class Solution4:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for start in range(i, -1, -1):
                end = n - 1 - (i - start)
                dp[i][start] = max(
                    nums[start] * multipliers[i] + dp[i + 1][start + 1],
                    nums[end] * multipliers[i] + dp[i + 1][start]
                )
        return dp[0][0]


# DP - top down with only two state variables (end is calculated dynamically)
class Solution3:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = [[inf for _ in range(len(nums))] for _ in range(len(multipliers))]
        return self.dp(nums, multipliers, 0, 0, memo)

    def dp(self, nums, multipliers, start, m, memo):
        end = len(nums) - 1 - (m - start)
        if m == len(multipliers) - 1:
            return max(nums[start] * multipliers[m], nums[end] * multipliers[m])
        if memo[m][start] != inf:
            return memo[m][start]
        memo[m][start] = max(
            nums[start] * multipliers[m] + self.dp(nums, multipliers, start + 1, m + 1, memo),
            nums[end] * multipliers[m] + self.dp(nums, multipliers, start, m + 1, memo)
        )
        return memo[m][start]


# DP - top down
# accepted but not optimal > 1300m and best solutions are around 700ms
class Solution2:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = {}
        return self.dp(nums, multipliers, 0, len(nums) - 1, 0, memo)

    def dp(self, nums, multipliers, start, end, m, memo):
        if m == len(multipliers) - 1:
            return max(nums[start] * multipliers[m], nums[end] * multipliers[m])
        key = f"{m}:{start}:{end}"
        if key in memo:
            return memo[key]
        memo[key] = max(
            nums[start] * multipliers[m] + self.dp(nums, multipliers, start + 1, end, m + 1, memo),
            nums[end] * multipliers[m] + self.dp(nums, multipliers, start, end - 1, m + 1, memo)
        )
        return memo[key]


# naive recurrence solution but refactored toward dp to use indexes instead of arrays slicing
class Solution1:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        return self.dp(nums, multipliers, 0, len(nums) - 1, 0)

    def dp(self, nums, multipliers, start, end, m):
        if m == len(multipliers) - 1:
            return max(nums[start] * multipliers[m], nums[end] * multipliers[m])
        return max(
            nums[start] * multipliers[m] + self.dp(nums, multipliers, start + 1, end, m + 1),
            nums[end] * multipliers[m] + self.dp(nums, multipliers, start, end - 1, m + 1)
        )


# naive recurrence solution
# TLE
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        if len(multipliers) == 1:
            return max(nums[0] * multipliers[0], nums[-1] * multipliers[0])
        return max(
            nums[0] * multipliers[0] + self.maximumScore(nums[1:], multipliers[1:]),
            nums[-1] * multipliers[0] + self.maximumScore(nums[:-1], multipliers[1:])
        )


if __name__ == "__main__":
    s = Solution4()
    # assert s.maximumScore([1, 2, 3], [3, 2, 1]) == 14
    assert s.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]) == 102
    # assert s.maximumScore([-51, 2], [2]) == 4
    # assert s.maximumScore(
    #     [830, 388, 289, 14, -221, 610, 163, 444, -750, -217, -235, -882, 746, -907, 67, -71, -990, 400, -54, -114, -100,
    #      233, 667, 612, -812, -471, -639, -306, -95, 524, -198, -520, -652, 704, -697, -43, -539, -105, -160, 838, 499,
    #      -109, -977, 975, 658, -250, 593, 154, -777, 496, 747, 307, -340, 403, -749, -185, 721, 327, -851, -112, 770,
    #      -14, 754, -242, -220, -776, -66, 348, -707, -693, 9, -354, 741, 129, 234, 638, 404, -408, -30, 422, -234, 818,
    #      -627, 706, -752, -699, -773, -786, 241, 432, 273, 272, -57, 878, -149, -547, 491, 519, 870, 700, 476, -99, 902,
    #      -878, -237, -549, 445, -372, 277, -486, 872, -569, -687, 339, 653, -564, 862, 898, -962, 306, 668, -143, 344,
    #      -312, 108, -536, -453, -52, 627, -225, -28, 403, -422, 367, 133, 970, -575, 353, 347, 275, -876, 337, 594, 441,
    #      -498, -875, -934, 133],
    #     [-844, -363, 797, 480, 141, 733, -935, 842, 160, -928, 787, -895, -742, -963, 889, -713, -264, -400, 117, 163,
    #      68, -286, -810, -365, 180, -690, -558, -409, 290, 51, -272, -454, -110, 850, 578, 131, -913, 675, 817, 380,
    #      410, 860, -441, 56, -80, -650, -474, 858, 269]
    # ) == 11042056
