from typing import List


# 哈希计数
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 对短数组哈希计数，减少内存
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        count_dict = {}
        for num in nums1:
            count_dict[num] = count_dict.get(num, 0) + 1

        res = []
        for num in nums2:
            count = count_dict.get(num, 0)
            if count > 0:
                res.append(num)
                count_dict[num] = count - 1

        return res


# 排序双指针
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i1 = i2 = 0
        res = []

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1

        return res


solution = Solution()
print(solution.intersect([1, 2, 2, 1], [2, 2]))
