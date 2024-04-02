from functools import cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def next_day(i, shift):
            d = days[i]
            while i < len(days) and days[i] < d + shift:
                i += 1
            return i

        @cache
        def dp(current_day):
            if current_day >= len(days):
                return 0
            min_cost = int(1e9)
            for ticket, period in [(0, 1), (1, 7), (2, 30)]:
                min_cost = min(min_cost, costs[ticket] + dp(next_day(current_day, period)))
            return min_cost

        return dp(0)


if __name__ == "__main__":
    s = Solution()
    assert s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
    assert s.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17
