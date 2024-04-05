from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        inf = int(1e9)
        if n == 1:
            return 0

        @cache
        def dp(current, clipboard):
            if current > n:
                return inf
            if current == n:
                return 0
            return min(
                2 + dp(current + current, current),  # copy and paste = 2 operation
                1 + dp(current + clipboard, clipboard)  # paste = 1 operation
            )

        return dp(1, 1) + 1  # first operation must be a copy since the clipboard is empty


if __name__ == "__main__":
    s = Solution()
    assert s.minSteps(3) == 3
    assert s.minSteps(1) == 0
    assert s.minSteps(4) == 4
    assert s.minSteps(5) == 5
    assert s.minSteps(6) == 5
    assert s.minSteps(12) == 7
    assert s.minSteps(30) == 10
    assert s.minSteps(55) == 16
    assert s.minSteps(200) == 16
    assert s.minSteps(350) == 19
