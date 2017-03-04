from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums
        rob_max_arr = [0, nums[1]]

        for i in range(2, len(nums)):
            rob_max = max(rob_max_arr[i - 2] + nums[i], rob_max_arr[i - 1])
            rob_max_arr.append(rob_max)

        return rob_max_arr.pop()


# 简洁
class Solution1:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0

        for num in nums:
            prev, curr = curr, max(prev + num, curr)

        return curr


solution = Solution1()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
