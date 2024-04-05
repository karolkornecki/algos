from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(t, current, start):
            if t == 0 and len(current) == k:
                result.append([*current])
                return
            if t <= 0 or start > 9 or len(current) >= k:
                return
            for num in range(start, 10):
                current.append(num)
                backtrack(t - num, current, num + 1)
                current.pop()

        backtrack(n, [], 1)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
