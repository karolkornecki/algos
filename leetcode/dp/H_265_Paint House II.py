from functools import cache
from typing import List


# DP top-down
# take a look at 256. Paint House problem
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        number_of_colors = len(costs[0])

        @cache
        def dp(house_no, excluded_color) -> int:
            if house_no >= len(costs):
                return 0
            min_cost = int(1e9)
            for color in range(number_of_colors):
                if color != excluded_color:
                    min_cost = min(min_cost, costs[house_no][color] + dp(house_no + 1, color))
            return min_cost

        return dp(0, -1)


if __name__ == "__main__":
    s = Solution()
    assert s.minCostII([[1, 5, 3], [2, 9, 4]]) == 5
    assert s.minCostII([[1, 3], [2, 4]]) == 5
