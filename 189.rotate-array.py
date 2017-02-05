from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        for _ in range(k):
            nums.insert(0, nums.pop())

        print(nums)


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
