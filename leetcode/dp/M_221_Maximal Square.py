import math
from typing import List


# DP - top down
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[int(col) for col in row] for row in matrix]
        max_area = 0

        # bottom up DP
        for r in range(0, rows):
            for c in range(0, cols):
                if r != 0 and c != 0:
                    if int(dp[r][c]) == 0:
                        dp[r][c] = 0
                    else:
                        dp[r][c] = int(pow(math.sqrt(min(min(dp[r][c - 1], dp[r - 1][c]), dp[r - 1][c - 1])) + 1, 2))
                max_area = max(max_area, dp[r][c])
        return max_area


if __name__ == "__main__":
    s = Solution()
    assert s.maximalSquare(
        [["1", "0", "1", "1", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "1", "1", "1", "1"]]) == 9
    assert s.maximalSquare([["0", "1"], ["1", "0"]]) == 1
    assert s.maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]) == 4
    assert s.maximalSquare(
        [["1", "1", "1", "1", "0"],
         ["1", "1", "1", "1", "0"],
         ["1", "1", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["0", "0", "1", "1", "1"]]
    ) == 16
