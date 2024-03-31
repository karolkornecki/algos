from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        alphabet = ['a', 'e', 'i', 'o', 'u']

        @cache
        def dp(i, prev_letter) -> int:
            if i >= n:
                return 1
            count = 0
            for letter in alphabet:
                if prev_letter == 'a' and letter != 'e':
                    continue
                if prev_letter == 'e' and letter not in ['a', 'i']:
                    continue
                if prev_letter == 'i' and letter == 'i':
                    continue
                if prev_letter == 'o' and letter not in ['i', 'u']:
                    continue
                if prev_letter == 'u' and letter != 'a':
                    continue
                count += dp(i + 1, letter)
            return count

        return dp(0, '') % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    assert s.countVowelPermutation(1) == 5
    assert s.countVowelPermutation(2) == 10
    assert s.countVowelPermutation(5) == 68
