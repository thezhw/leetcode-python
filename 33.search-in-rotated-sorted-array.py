from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 没旋转，为0
        rotate_idx = 0

        # 寻找旋转点，即左边元素值大于当前元素值的位置
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid - 1] > nums[mid]:
                rotate_idx = mid
                break
            elif nums[0] < nums[mid]:  # 旋转点在 mid 的右边
                left += 1
            else:
                right -= 1

        # 搜索旋转点左边数组
        left, right = 0, rotate_idx - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1

        # 搜索旋转点右边数组
        left, right = rotate_idx, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1

        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(solution.search([4, 5, 6, 7, 0, 1, 2], 5))
