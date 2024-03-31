from functools import cache


# DP - top-down
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(dice_left, target_left) -> int:
            if target_left == 0 and dice_left == 0:
                return 1
            if target_left < 0 or dice_left == 0:
                return 0
            count = 0
            for i in range(1, k + 1):
                count += dp(dice_left - 1, target_left - i)
            return count

        return dp(n, target) % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    assert s.numRollsToTarget(1, 6, 3) == 1
    assert s.numRollsToTarget(2, 6, 7) == 6
    assert s.numRollsToTarget(12, 3, 5) == 0
    assert s.numRollsToTarget(30, 30, 500) == 222616187
