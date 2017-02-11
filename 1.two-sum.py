from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                return [diffs.get(diff), i]
            else:
                diffs[nums[i]] = i


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
