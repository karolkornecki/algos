class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # trick with arrays 1 longer than strings to avoid many conditions
        # inside nested loop for i and j equals 0 to avoid out of range
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                # normalize indexes because i started from 1 in dp matrix but string starts with 0
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("ace", "abcde") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    assert s.longestCommonSubsequence("abbcdef", "bd") == 2
