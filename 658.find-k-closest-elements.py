from typing import List


# 排除法
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left, right = 0, size - 1

        for _ in range(size - k):
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1

        return arr[left:left + k]


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left, right = 0, size - k

        while left < right:
            mid = (left + right) // 2

            # 在 [mid, mid + k] 区间内 x 离右端点更近
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


solution = Solution1()
print(solution.findClosestElements([0, 1, 2, 3, 4, 5, 6, 7], 3, 6))
print(solution.findClosestElements([0, 1, 2, 3, 4, 5, 6, 7], 3, 1))
