from functools import cache


# DP top-down
class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        ways = self.numDecodings(s[1:])
        if int(s[0:2]) <= 26:
            ways += self.numDecodings(s[2:])
        return ways


if __name__ == '__main__':
    s = Solution()
    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
    assert s.numDecodings("2212") == 5
    assert s.numDecodings("2202") == 1
    assert s.numDecodings("06") == 0
