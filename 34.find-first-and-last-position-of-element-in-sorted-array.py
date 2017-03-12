from typing import List


# 线性扫描
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx, right_idx = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]


# 二分查找
class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left_idx, right_idx = -1, -1

        # 查找最左则边界 搜索范围 [1, len(nums) - 1]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target and nums[mid - 1] != target:
                left_idx = mid
                break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[0] == target:
            left_idx = 0
        if left_idx == -1 and nums[len(nums) - 1] == target:
            left_idx = len(nums) - 1

        # 查找最右侧边界 搜索范围 [0, len(nums) - 2]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and nums[mid + 1] != target:
                right_idx = mid
                break
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid  # 每一次循环 right 都是取不到的

        if nums[len(nums) - 1] == target:
            right_idx = len(nums) - 1

        return [left_idx, right_idx]


solution = Solution1()
print(solution.searchRange([2, 2], 2))
