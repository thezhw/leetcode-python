from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 寻找大于等于 target 值的第一个位置
        while left < right:
            mid = (left + right) // 2  # 取左中位数

            if nums[mid] < target:  # 分支逻辑先过滤掉左中位数
                left = mid + 1
            else:
                right = mid

        return left if nums[left] >= target else left + 1


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 5))
print(solution.searchInsert([1, 3, 5, 6], 2))
print(solution.searchInsert([1, 3, 5, 6], 7))
print(solution.searchInsert([1, 3, 5, 6], 0))
