from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtrack(t: int, current: List[int], i: int):
            if t < 0:
                return
            if t == 0:
                result.append([*current])
                return
            for i in range(i, n):
                current.append(candidates[i])
                backtrack(t - candidates[i], current, i)
                current.pop()

        backtrack(target, [], 0)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
