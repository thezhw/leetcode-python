from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        inter = []
        left, right = 0, 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                inter.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1

        return inter


solution = Solution()
print(solution.intersect([1, 2, 2, 1], [2, 2]))
