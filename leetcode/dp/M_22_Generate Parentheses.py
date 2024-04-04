from typing import List


# It's not DP problem, I think hmm?
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dp(open_left, closed_left, s):
            # end
            if open_left == 0 and closed_left == 0:
                result.append(s)
                return
            # can only close
            if open_left == 0 and closed_left > 0:
                dp(open_left, closed_left - 1, f"{s})")
                return
            # have balance I can only open
            if 0 < open_left == closed_left > 0:
                dp(open_left - 1, closed_left, f"{s}(")
                return
            dp(open_left - 1, closed_left, f"{s}(")
            dp(open_left, closed_left - 1, f"{s})")

        dp(n, n, "")
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert s.generateParenthesis(1) == ["()"]
