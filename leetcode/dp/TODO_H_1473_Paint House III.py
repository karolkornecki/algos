from functools import cache
from typing import List


class Solution:
    # TODO
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf = int(1e9)

        @cache
        def dp(house_no, prev_house_color, neighs_so_far) -> int:
            if neighs_so_far > target:
                return inf
            if house_no >= m:  # all houses painted
                return 0
            if houses[house_no] != 0:  # house cannot be painted
                return 0

            min_cost = inf
            for color in range(n):
                # if color == prev -> next_house, color/(or..), neighbourhoods
                # else             -> next_house, color/(or..), neighbourhoods+1 or nor
                min_cost = min(min_cost, cost[house_no][color] + dp(house_no + 1))
            return min_cost

        return dp(0, 0, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.minCost([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3) == 9
    # assert s.minCost([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3) == 3
