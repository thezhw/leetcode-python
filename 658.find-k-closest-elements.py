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


solution = Solution()
print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
