from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        current_profit = 0
        for i in range(1, len(prices)):
            current_profit = max(current_profit, prices[i] - min_price)
            max_profit = max(max_profit, current_profit)
            min_price = min(min_price, prices[i])
        return max_profit


if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([7]) == 0
