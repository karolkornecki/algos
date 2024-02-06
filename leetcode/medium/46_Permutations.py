from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        self.backtrack(nums, set(), [], result)
        return result

    def backtrack(self, nums, used, current, result):
        if len(current) == len(nums):
            result.append(current.copy())
            return
        for i in range(len(nums)):
            if i not in used:
                current.append(nums[i])
                used.add(i)
                self.backtrack(nums, used, current, result)
                current.pop()
                used.remove(i)


if __name__ == '__main__':
    s = Solution()
    r = s.permute([1, 2, 3, 4, 5])
    # r = s.permute([1])
    for e in r:
        print(e)
