from functools import cache


# DP top-down
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dp(a, b, c):
            # already reach the end of string
            if a >= len(s1) - 1 and b >= len(s2) - 1 and c >= len(s3):
                return True
            # both s1 and s2 have matching character we need to check both paths
            if a < len(s1) and b < len(s2) and c < len(s3) and s1[a] == s2[b] == s3[c]:
                return dp(a + 1, b, c + 1) or dp(a, b + 1, c + 1)
            if a < len(s1) and c < len(s3) and s1[a] == s3[c]:
                return dp(a + 1, b, c + 1)
            if b < len(s2) and c < len(s3) and s2[b] == s3[c]:
                return dp(a, b + 1, c + 1)
            return False

        return dp(0, 0, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.isInterleave("a", "aab", "aaba")
    assert not s.isInterleave("a", "", "c")
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    assert not s.isInterleave(
        "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
        "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
        "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
