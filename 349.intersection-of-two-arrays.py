from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i1 = i2 = 0
        ans = []

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif not ans or ans[len(ans) - 1] != nums1[i1]:
                ans.append(nums1[i1])
            else:
                i1 += 1
                i2 += 1

        return ans


solution = Solution()
print(solution.intersection([1, 2, 2, 1], [2, 2]))
