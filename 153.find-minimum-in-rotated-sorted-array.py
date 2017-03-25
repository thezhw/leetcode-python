from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # 因 left < right，所以 left = right = len(nums) - 1 不可能
            # 即 mid + 1 不可能越界
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[left]:  # mid 处于最小值得左边
                left = mid + 1
            else:
                right = mid

        return nums[0]


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left] and nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


solution = Solution1()
print(solution.findMin([2, 3, 1]))
print(solution.findMin([3, 4, 5, 1, 2]))
print(solution.findMin([0, 1, 2, 3, 4]))
print(solution.findMin([1, 2, 3, 4, 0]))
