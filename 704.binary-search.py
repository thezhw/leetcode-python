from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2  # mid 取左中位数
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1 if nums[left] != target else left


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2  # mid 取右中位数
            print(mid, nums[mid])
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return -1 if nums[left] != target else left


solution = Solution1()
print(solution.search([0, 1, 2, 3, 4, 5], 0))
