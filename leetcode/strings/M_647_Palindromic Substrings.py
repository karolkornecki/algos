# TODO Manacher's

class Solution1:
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        for i in range(n):
            count += 1
            left = i - 1
            right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                left -= 1
                right += 1
        return count


# yet better approach ~192ms run memory 25.1mb
class Solution2:
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # start at right most bottom corner and move up
        for row in range(n, -1, -1):
            for col in range(row, n):
                # single char is always valid palindrome
                if row == col:
                    dp[row][col] = True
                # 2 characters string is a valid palindrome when chars are the same
                elif row + 1 == col:
                    dp[row][col] = s[row] == s[col]
                # leftmost and rightmost chars are the same and string between is a palindrome
                elif s[row] == s[col] and dp[row + 1][col - 1]:
                    dp[row][col] = True
                if dp[row][col]:
                    count += 1
        return count


# much better approach with cache ~322ms run memory 17.1mb
class Solution3:
    def countSubstrings(self, s: str) -> int:
        cache = set()
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.isPalindrome(s[i:j], cache):
                    count += 1
        return count

    def isPalindrome(self, s, cache):
        if s in cache:
            return True
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        cache.add(s)
        return True


# naive approach - very low performance over 4276ms run, memory 16.5mb
class Solution4:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    count += 1
        return count

    def isPalindrome(self, t):
        lo = 0
        hi = len(t) - 1
        while lo <= hi:
            if t[lo] != t[hi]:
                return False
            lo += 1
            hi -= 1
        return True


if __name__ == '__main__':
    s = Solution1()
    print(s.countSubstrings("aaaaa"))
