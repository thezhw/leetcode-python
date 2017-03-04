from typing import List


# 暴力
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = float('-inf')

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total > total_max:
                    total_max = total

        return total_max


# 一次遍历
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = float('-inf')
        total = 0

        for num in nums:
            total = max(total + num, num)  # 子序和 只有两种情况
            if total > total_max:
                total_max = total

        return total_max


solution = Solution1()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
