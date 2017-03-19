from typing import List


# 排序
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

        return -1


# 二分查找
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                left = mid + 1
            else:
                right = mid

        return left


solution = Solution1()
print(solution.findDuplicate([1, 3, 4, 2, 4]))
