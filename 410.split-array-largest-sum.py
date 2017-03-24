from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        # 以 sums_max 为最大值至少要分多少组
        def group(sums_max):
            sums, cnt = 0, 1
            for num in nums:
                if sums + num > sums_max:
                    cnt += 1
                    sums = num
                else:
                    sums += num

            return cnt

        # 分 len(nums) 组， 分 1 组时 和的最大值
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if group(mid) <= m:
                right = mid
            else:
                left = mid + 1

        return left


solution = Solution()
print(solution.splitArray([7, 2, 5, 10, 8], 2))
