from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            # 左右边界相等
            if nums[left] == nums[right]:
                right -= 1
                continue

            mid = left + (right - left) // 2

            # 当前数 > 大于后继数
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] >= nums[left]:  # mid 处于最小值得左边
                left = mid + 1
            else:
                right = mid

        return nums[0]


solution = Solution()
print(solution.findMin([1, 0, 1, 1, 1]))
print(solution.findMin([1, 1, 1, 0, 1]))
