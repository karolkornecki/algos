from functools import cache
from typing import List


# DP top-down
# state: let dp(i, c) is the minimum cost of painting houses up to i-th index excluding color
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(house_no, excluded_color) -> int:
            if house_no >= len(costs):
                return 0
            min_cost = int(1e9)
            for color in range(3):
                if color != excluded_color:
                    min_cost = min(min_cost, costs[house_no][color] + dp(house_no + 1, color))
            return min_cost

        # -1 mean that none of the color is excluded
        return dp(0, -1)


if __name__ == "__main__":
    s = Solution()
    assert s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
    assert s.minCost([[7, 6, 2]]) == 2
