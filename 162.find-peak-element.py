from typing import List


# 线性扫描
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


# 二分查找
class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:  # 上升序列
                left = mid + 1
            else:  # 下降序列
                right = mid

        return left


solution = Solution1()
print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
