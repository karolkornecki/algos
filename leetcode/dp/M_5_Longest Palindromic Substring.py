# DP bottom-up -> see also: M_647_Palindromic Substrings
class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_length = int(-1e9)
        max_palindrome = None
        for start in range(n, -1, -1):
            for end in range(start, n):
                # single char is always valid palindrome
                if start == end:
                    dp[start][end] = True
                # two length string is valid palindrome iff both chars are the same
                elif start + 1 == end and s[start] == s[end]:
                    dp[start][end] = True
                # if leftmost and rightmost chars are the same and string in the middle is valid palindrome then
                elif s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                if dp[start][end]:
                    if end - start + 1 > max_length:
                        max_length = end - start + 1
                        max_palindrome = s[start:end + 1]

        return max_palindrome


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome('babad') == 'aba'
    assert s.longestPalindrome('abbcbba') == 'abbcbba'
