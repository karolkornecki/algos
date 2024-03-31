from typing import List


# DP bottom-up
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] max length of subarray up to i and j respectively (nums1[:i], nums2[j:]
        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
        # find max in matrix
        return max(max(r) for r in dp)


if __name__ == "__main__":
    s = Solution()
    assert s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
    assert s.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5
    assert s.findLength([0, 0, 0, 0, 0], [0, 0, 0]) == 3
    assert s.findLength([1, 2, 0], [3]) == 0
    assert s.findLength([2, 1, 0, 0, 0], [1, 0, 0]) == 3
    assert s.findLength([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]) == 9
