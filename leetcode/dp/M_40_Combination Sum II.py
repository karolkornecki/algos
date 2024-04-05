from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []

        def backtrack(t, current, i):
            if t == 0 and current not in result:
                result.append([*current])
                return
            if t < 0 or i >= n:
                return
            prev = None
            for c in range(i, n):
                if candidates[c] != prev:
                    prev = candidates[c]
                    current.append(candidates[c])
                    backtrack(t - candidates[c], current, c + 1)
                    current.pop()

        backtrack(target, [], 0)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
